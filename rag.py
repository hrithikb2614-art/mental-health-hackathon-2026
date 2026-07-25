"""Retrieval-augmented generation over documents stored in Supabase.

Requires three secrets (see .streamlit/secrets.toml.example):
- SUPABASE_URL, SUPABASE_KEY: a Supabase project with the schema in sql/schema.sql applied
- OPENAI_API_KEY: used for both embeddings (text-embedding-3-small) and chat answers

Document uploads are admin-curated: the parsed, chunked, and embedded content is
written to Supabase and shared by every visitor who asks the AI Assistant a question.
"""

import streamlit as st

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

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


def _has_secret(key: str) -> bool:
    try:
        return key in st.secrets
    except Exception:
        # Raised when no secrets.toml exists at all rather than an empty one.
        return False


def is_configured() -> bool:
    return all(
        _has_secret(key) for key in ("SUPABASE_URL", "SUPABASE_KEY", "OPENAI_API_KEY")
    )


def missing_secrets() -> list:
    return [
        key
        for key in ("SUPABASE_URL", "SUPABASE_KEY", "OPENAI_API_KEY")
        if not _has_secret(key)
    ]


def get_secret(key: str, default=None):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


@st.cache_resource
def get_supabase_client():
    from supabase import create_client

    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])


@st.cache_resource
def get_openai_client():
    from openai import OpenAI

    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


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
    client = get_openai_client()
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


def upsert_document(filename: str, text: str) -> int:
    """Chunk, embed, and store a document's text in Supabase. Returns chunk count."""
    chunks = chunk_text(text)
    if not chunks:
        return 0
    embeddings = embed_texts(chunks)
    rows = [
        {
            "source": filename,
            "chunk_index": i,
            "content": chunk,
            "embedding": embedding,
        }
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
    ]
    supabase = get_supabase_client()
    supabase.table("documents").insert(rows).execute()
    return len(rows)


def search_similar(query: str, match_count: int = 5) -> list:
    query_embedding = embed_texts([query])[0]
    supabase = get_supabase_client()
    result = supabase.rpc(
        "match_documents",
        {"query_embedding": query_embedding, "match_count": match_count},
    ).execute()
    return result.data or []


def generate_answer(question: str, matches: list) -> str:
    client = get_openai_client()
    if matches:
        context = "\n\n".join(
            f"[Source: {m['source']}]\n{m['content']}" for m in matches
        )
    else:
        context = "(No matching reference excerpts were found in the knowledge base.)"

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Reference excerpts:\n{context}\n\nQuestion: {question}",
            },
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
