"""
What Is LlamaIndex?
====================
Run: python3 01_what_is_llamaindex.py

Covers:
- What LlamaIndex is and what problem it solves
- The three-stage pipeline: Ingestion → Indexing → Querying
- Core philosophy: "Your data, your LLM, connected"
- Where LlamaIndex fits in the AI ecosystem (2026)
"""


# =============================================================================
# WHAT IS LLAMAINDEX?
# =============================================================================

print("=" * 55)
print("  WHAT IS LLAMAINDEX?")
print("=" * 55)

print("""
  LlamaIndex is a data framework for LLM applications.

  The Problem It Solves:
  ─────────────────────
  LLMs (GPT-4, Claude, etc.) are powerful but they:
    • Don't know YOUR data (internal docs, databases, APIs)
    • Have knowledge cutoff dates
    • Can't access real-time information
    • Hallucinate when they don't know something

  LlamaIndex bridges the gap between YOUR DATA and LLMs.
""")


# =============================================================================
# THE THREE-STAGE PIPELINE
# =============================================================================

print("=" * 55)
print("  THE THREE-STAGE PIPELINE")
print("=" * 55)

print("""
  Every LlamaIndex application follows this pattern:

  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
  │  INGESTION  │───▶│  INDEXING   │───▶│  QUERYING   │
  │             │    │             │    │             │
  │ Load data   │    │ Chunk text  │    │ Retrieve    │
  │ from any    │    │ Generate    │    │ relevant    │
  │ source      │    │ embeddings  │    │ context     │
  │             │    │ Store in    │    │ Generate    │
  │             │    │ vector DB   │    │ answer      │
  └─────────────┘    └─────────────┘    └─────────────┘

  Stage 1 — INGESTION:
    Load documents from PDFs, websites, databases, APIs, etc.

  Stage 2 — INDEXING:
    Split documents into chunks, generate vector embeddings,
    and store them in a searchable index.

  Stage 3 — QUERYING:
    User asks a question → retrieve relevant chunks →
    LLM generates answer grounded in YOUR data.

  This is called RAG: Retrieval-Augmented Generation.
""")


# =============================================================================
# CORE ABSTRACTIONS
# =============================================================================

print("=" * 55)
print("  CORE ABSTRACTIONS")
print("=" * 55)

print("""
  LlamaIndex has 5 key abstractions:

  1. Documents   — Your raw data (a PDF, webpage, database row)
  2. Nodes       — Chunks of a document (paragraphs, sentences)
  3. Indices     — Data structures for efficient retrieval
  4. Embeddings  — Numeric vectors representing meaning
  5. Query Engines — The interface for asking questions

  Think of it like a library:
    Documents = Books
    Nodes     = Pages/Paragraphs
    Index     = Card catalog
    Embedding = The "meaning fingerprint" of each page
    Query     = Asking the librarian a question
""")


# =============================================================================
# WHERE LLAMAINDEX FITS (2026)
# =============================================================================

print("=" * 55)
print("  WHERE LLAMAINDEX FITS (2026 ECOSYSTEM)")
print("=" * 55)

print("""
  ┌──────────────────────────────────────────────────────┐
  │           AI APPLICATION STACK                        │
  ├──────────────────────────────────────────────────────┤
  │                                                       │
  │  Orchestration:  LangGraph, CrewAI, custom code       │
  │                  (complex multi-step workflows)       │
  │                                                       │
  │  Data + RAG:     LlamaIndex  ◄── YOU ARE HERE         │
  │                  (ingestion, indexing, retrieval)      │
  │                                                       │
  │  LLM Providers:  OpenAI, Anthropic, Mistral, etc.    │
  │                  (the intelligence layer)              │
  │                                                       │
  │  Vector Stores:  Pinecone, Chroma, Qdrant, Weaviate  │
  │                  (the storage layer)                   │
  │                                                       │
  └──────────────────────────────────────────────────────┘

  Key Insight:
    LlamaIndex is the DATA layer. It's always needed.
    The question is whether you need orchestration on top.

    70% of RAG apps: LlamaIndex alone is sufficient.
    30% of apps:     LlamaIndex + LangGraph for complex workflows.
""")


# =============================================================================
# WHAT YOU'LL BUILD IN THIS COURSE
# =============================================================================

print("=" * 55)
print("  WHAT YOU'LL BUILD IN THIS COURSE")
print("=" * 55)

print("""
  By the end of this course, you'll be able to build:

    ✓ Document Q&A systems (ask questions about your PDFs)
    ✓ Semantic search engines (find meaning, not just keywords)
    ✓ AI agents with tools (calculators, APIs, databases)
    ✓ Production RAG APIs (FastAPI + caching + monitoring)
    ✓ Evaluation pipelines (measure and improve quality)

  Prerequisites:
    • Python 3.9+
    • Basic Python knowledge (functions, classes, pip)
    • An OpenAI API key or equivalent(for embeddings and LLM calls)

  Next: Run 02_five_line_rag.py to see LlamaIndex in action!
""")

print("=" * 55)
print("  ✓ Complete! Next: python3 02_five_line_rag.py")
print("=" * 55)
