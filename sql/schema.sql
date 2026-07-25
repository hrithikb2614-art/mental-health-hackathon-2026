-- Run this once in your Supabase project's SQL editor (Project > SQL Editor > New query)
-- before using the AI Assistant tab. Requires the pgvector extension, which Supabase
-- ships by default.

create extension if not exists vector;

create table if not exists documents (
    id bigint generated always as identity primary key,
    source text not null,           -- original filename
    chunk_index int not null,       -- position of this chunk within the source document
    content text not null,          -- the chunk of text
    embedding vector(1536),         -- OpenAI text-embedding-3-small dimension
    created_at timestamptz not null default now()
);

create index if not exists documents_embedding_idx
    on documents
    using ivfflat (embedding vector_cosine_ops)
    with (lists = 100);

-- RPC used by the app to fetch the most relevant chunks for a question.
create or replace function match_documents (
    query_embedding vector(1536),
    match_count int default 5
)
returns table (
    id bigint,
    source text,
    chunk_index int,
    content text,
    similarity float
)
language sql stable
as $$
    select
        documents.id,
        documents.source,
        documents.chunk_index,
        documents.content,
        1 - (documents.embedding <=> query_embedding) as similarity
    from documents
    order by documents.embedding <=> query_embedding
    limit match_count;
$$;
