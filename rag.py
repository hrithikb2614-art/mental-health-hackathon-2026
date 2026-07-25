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
CHAT_MAX_TOKENS = 1024
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

KNOWLEDGE_BASE_PATH = Path(__file__).parent / "data" / "knowledge_base.json"

SYSTEM_PROMPT = (
    "You are a supportive assistant answering questions using only the reference "
    "excerpts provided below. You are not a doctor or therapist and must not "
    "diagnose, prescribe, or claim certainty about someone's health. If the "
    "excerpts don't contain a real answer, say so plainly instead of guessing. "
    "Keep answers concise, cite which source each claim comes from by filename, "
    "and end every answer by encouraging the person to talk to a qualified "
    "professional for anything health-related. If the question suggests the "
    "person may be in crisis or thinking of self-harm, say clearly that their "
    "safety matters most and point them to the 988 Suicide & Crisis Lifeline "
    "(call or text 988) before anything else."
)


CRISIS_KEYWORDS = (
    "suicide", "kill myself", "end my life", "self-harm", "self harm",
    "hurt myself", "hurting myself", "don't want to be here", "want to die",
)


def contains_crisis_language(text: str) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in CRISIS_KEYWORDS)


def _secrets_read_error() -> str:
    """Return a description of a real problem reading secrets.toml, or "" if it's fine
    (including the normal case of no secrets.toml existing at all)."""
    try:
        list(st.secrets.keys())
        return ""
    except Exception as exc:
        message = str(exc)
        if "parsing secrets file" in message.lower():
            return f"secrets.toml has a syntax error: {message}"
        return ""  # no secrets.toml at all is expected/normal, not an error


def _has_secret(key: str) -> bool:
    try:
        return key in st.secrets
    except Exception:
        return False


def is_configured() -> bool:
    return not _secrets_read_error() and _has_secret("ANTHROPIC_API_KEY")


def missing_secrets() -> list:
    return [] if _has_secret("ANTHROPIC_API_KEY") else ["ANTHROPIC_API_KEY"]


def setup_issue() -> str:
    """Human-readable explanation of why the AI Assistant isn't configured, or "" if it is."""
    read_error = _secrets_read_error()
    if read_error:
        return read_error
    if not _has_secret("ANTHROPIC_API_KEY"):
        return (
            "Add `ANTHROPIC_API_KEY` to `.streamlit/secrets.toml` — see "
            "`.streamlit/secrets.toml.example` for setup."
        )
    return ""


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


def generate_answer(question: str, matches: list) -> str:
    client = get_anthropic_client()
    if matches:
        context = "\n\n".join(
            f"[Source: {m['source']}]\n{m['content']}" for m in matches
        )
    else:
        context = "(No matching reference excerpts were found in the knowledge base.)"

    response = client.messages.create(
        model=CHAT_MODEL,
        max_tokens=CHAT_MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Reference excerpts:\n{context}\n\nQuestion: {question}",
            },
        ],
        temperature=0.3,
    )
    return response.content[0].text
