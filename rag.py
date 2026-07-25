"""Retrieval-augmented generation over documents stored in a local JSON file.

Requires one secret (see .streamlit/secrets.toml.example):
- ANTHROPIC_API_KEY: used for chat answers (Claude)

Embeddings are generated locally with a sentence-transformers model, so no
second API key or account is needed for document search.

No external account or database setup needed. Document uploads are
admin-curated: parsed, chunked, and embedded content is saved to a local
JSON file (data/knowledge_base.json) and shared by every visitor who asks
the AI Assistant a question, for as long as the app process keeps running.
The file is gitignored, and resets if the app is redeployed.
"""

import json
from pathlib import Path

import numpy as np
import streamlit as st

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHAT_MODEL = "claude-sonnet-5"
CHAT_MAX_TOKENS = 1536
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

KNOWLEDGE_BASE_PATH = Path(__file__).parent / "data" / "knowledge_base.json"

SYSTEM_PROMPT = (
    "You are a knowledgeable healthcare information assistant inside a physical- and "
    "mental-health symptom-checker app. Answer using two sources: (1) the reference "
    "excerpts provided below, when they're relevant — cite the source by name for any "
    "claim drawn from them — and (2) your own general medical and mental-health "
    "knowledge whenever the excerpts are missing, incomplete, or off-topic. Never refuse "
    "to answer a general health question just because the excerpts don't cover it; give "
    "a clear, accurate, well-explained answer either way, drawing on real clinical "
    "knowledge (mechanisms, typical symptoms, causes, red flags, standard treatment "
    "approaches, when to seek care). "
    "You are not a doctor or therapist: never diagnose a specific person, prescribe "
    "medication or dosages, or claim certainty about what someone individually has. "
    "Keep answers clear and appropriately thorough — a short paragraph or a few bullet "
    "points for straightforward questions, more detail for complex ones — and close by "
    "encouraging the person to confirm anything health-related with a qualified "
    "professional. Use the ongoing conversation history for context on follow-up "
    "questions. If the question suggests the person may be in crisis or thinking of "
    "self-harm, say clearly that their safety matters most and point them to the 988 "
    "Suicide & Crisis Lifeline (call or text 988) before anything else."
)


CRISIS_KEYWORDS = (
    "suicide", "kill myself", "end my life", "self-harm", "self harm",
    "hurt myself", "hurting myself", "don't want to be here", "want to die",
)


def contains_crisis_language(text: str) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in CRISIS_KEYWORDS)


def _has_secret(key: str) -> bool:
    try:
        return key in st.secrets
    except Exception:
        # Raised when no secrets.toml exists at all rather than an empty one.
        return False


def is_configured() -> bool:
    return _has_secret("ANTHROPIC_API_KEY")


def missing_secrets() -> list:
    return [] if _has_secret("ANTHROPIC_API_KEY") else ["ANTHROPIC_API_KEY"]


def get_secret(key: str, default=None):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


@st.cache_resource
def get_anthropic_client():
    from anthropic import Anthropic

    return Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])


@st.cache_resource
def get_embedding_model():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(EMBEDDING_MODEL)


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list:
    """Split text into overlapping character-based chunks."""
    text = " ".join(text.split())
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = end - overlap
    return chunks


def extract_text(uploaded_file) -> str:
    """Extract plain text from an uploaded .txt, .md, or .pdf file."""
    name = uploaded_file.name.lower()
    if name.endswith(".pdf"):
        from pypdf import PdfReader

        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return uploaded_file.read().decode("utf-8", errors="ignore")


def embed_texts(texts: list) -> list:
    model = get_embedding_model()
    embeddings = model.encode(texts, normalize_embeddings=True)
    return embeddings.tolist()


def _load_store() -> list:
    if not KNOWLEDGE_BASE_PATH.exists():
        return []
    with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_store(store: list) -> None:
    KNOWLEDGE_BASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(KNOWLEDGE_BASE_PATH, "w", encoding="utf-8") as f:
        json.dump(store, f)


def store_stats() -> dict:
    store = _load_store()
    return {
        "chunks": len(store),
        "documents": len({row["source"] for row in store}),
    }


def _seed_default_knowledge_base() -> int:
    """Seed the knowledge base with this app's own curated health content, if empty."""
    if _load_store():
        return 0

    from health_data import DISEASES
    from kids_data import KIDS_THEMES

    documents = []
    for name, info in DISEASES.items():
        parts = [f"{name} ({info['category']} condition).", info["description"]]
        if info.get("mayo_summary"):
            parts.append(info["mayo_summary"])
        parts.append(f"Typical symptoms: {', '.join(info['symptoms'])}.")
        parts.append(f"Suggested next step: {info['advice']}")
        documents.append((f"app knowledge base: {name}", " ".join(parts)))

    for theme in KIDS_THEMES.values():
        text = f"{theme['title']}. {theme['blurb']} Tip: {theme['tip']}"
        documents.append((f"app knowledge base: Kids Check-In — {theme['title']}", text))

    # Embed everything in one batch call so a failure (e.g. no network to fetch the
    # embedding model) fails once, fast — instead of retrying per document.
    try:
        embeddings = embed_texts([text for _, text in documents])
    except Exception:
        return 0

    store = _load_store()
    store.extend(
        {"source": filename, "chunk_index": 0, "content": text, "embedding": embedding}
        for (filename, text), embedding in zip(documents, embeddings)
    )
    _save_store(store)
    return len(documents)


@st.cache_resource
def ensure_default_knowledge_base_seeded() -> int:
    """Run the default seeding exactly once per app process (cached across sessions)."""
    return _seed_default_knowledge_base()


def upsert_document(filename: str, text: str) -> int:
    """Chunk, embed, and append a document's text to the local store. Returns chunk count."""
    chunks = chunk_text(text)
    if not chunks:
        return 0
    embeddings = embed_texts(chunks)
    store = _load_store()
    store.extend(
        {
            "source": filename,
            "chunk_index": i,
            "content": chunk,
            "embedding": embedding,
        }
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
    )
    _save_store(store)
    return len(chunks)


def search_similar(query: str, match_count: int = 5) -> list:
    store = _load_store()
    if not store:
        return []

    query_embedding = np.array(embed_texts([query])[0])
    matrix = np.array([row["embedding"] for row in store])

    matrix_norms = np.linalg.norm(matrix, axis=1)
    matrix_norms[matrix_norms == 0] = 1e-10
    query_norm = np.linalg.norm(query_embedding) or 1e-10
    similarities = (matrix @ query_embedding) / (matrix_norms * query_norm)

    top_indices = np.argsort(-similarities)[:match_count]
    return [
        {**store[i], "similarity": float(similarities[i])}
        for i in top_indices
    ]


def generate_answer(question: str, matches: list, history: list = None, language: str = None) -> str:
    client = get_anthropic_client()
    if matches:
        context = "\n\n".join(
            f"[Source: {m['source']}]\n{m['content']}" for m in matches
        )
    else:
        context = (
            "(No matching reference excerpts were found in the knowledge base — answer "
            "from your own general medical/mental-health knowledge instead.)"
        )

    messages = [dict(turn) for turn in (history or [])]
    messages.append(
        {
            "role": "user",
            "content": f"Reference excerpts:\n{context}\n\nQuestion: {question}",
        }
    )

    system_prompt = SYSTEM_PROMPT
    if language and language != "English":
        system_prompt += f" Respond in {language}, regardless of what language the reference excerpts are in."

    response = client.messages.create(
        model=CHAT_MODEL,
        max_tokens=CHAT_MAX_TOKENS,
        system=system_prompt,
        messages=messages,
    )
    # Some models emit a thinking block ahead of the text block, so pick out
    # the text block(s) rather than assuming content[0] is text.
    text_blocks = [block.text for block in response.content if getattr(block, "type", None) == "text"]
    return "\n".join(text_blocks)
