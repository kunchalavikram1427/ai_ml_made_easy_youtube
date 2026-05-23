"""
Five-Line RAG Demo
===================
Run: python3 02_five_line_rag.py

Covers:
- Building a complete RAG system in just 5 lines of code
- The simplicity that makes LlamaIndex powerful
- Understanding what happens behind the scenes

Dependencies: pip install llama-index python-dotenv
"""

import os
import sys
import time

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from llama_index.core import VectorStoreIndex, Document, Settings
    from llama_index.llms.openai import OpenAI
    from llama_index.embeddings.openai import OpenAIEmbedding
    AVAILABLE = True
except ImportError:
    print("ERROR: pip install llama-index python-dotenv")
    print("Then set OPENAI_API_KEY in a .env file")
    sys.exit(1)

API_KEY = os.environ.get("OPENAI_API_KEY", "")
if not API_KEY or API_KEY.startswith("sk-your"):
    print("ERROR: Set OPENAI_API_KEY in .env file")
    sys.exit(1)

# Configure models
Settings.llm = OpenAI(model="gpt-5-mini", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")


# =============================================================================
# THE 5-LINE RAG SYSTEM
# =============================================================================

print("=" * 55)
print("  THE 5-LINE RAG SYSTEM")
print("=" * 55)

print("""
  The 5 lines that make up a complete RAG system:

  # LINE 1: Create documents
  documents = [Document(text="..."), ...]
  # LINE 2: Build index
  index = VectorStoreIndex.from_documents(documents)
  # LINE 3: Create query engine
  engine = index.as_query_engine()
  # LINE 4: Ask question
  response = engine.query("What is the pricing?")
  # LINE 5: Print answer
  print(response)

  Let's run it for real...
""")

start = time.time()

# ─── LINE 1: Create your documents ───────────────────────────────────────
documents = [
    Document(text="DataFlow Professional costs $199/month with unlimited pipelines."),
    Document(text="Refunds are available within 30 days of purchase."),
    Document(text="Enterprise customers get dedicated support with 4-hour SLA."),
    Document(text="Free trial lasts 14 days. No credit card required."),
    Document(text="DataFlow Starter plan is $49/month with up to 100 pipelines."),
    Document(text="Premium support includes phone and email assistance 24/7."),
    Document(text="All plans include real-time pipeline monitoring and analytics."),
    Document(text="Custom integrations are available for Enterprise tier customers."),
]

# ─── LINE 2: Build the index (chunks + embeds + stores) ─────────────────
index = VectorStoreIndex.from_documents(documents)

# ─── LINE 3: Create a query engine ──────────────────────────────────────
engine = index.as_query_engine()

# ─── LINE 4: Ask a question ─────────────────────────────────────────────
response = engine.query("What is the pricing?")

# ─── LINE 5: Get the answer ─────────────────────────────────────────────
print(f"  Answer: {response}")

elapsed = time.time() - start
print(f"\n  Time: {elapsed:.2f}s (includes embedding + LLM call)")


# =============================================================================
# WHAT HAPPENED BEHIND THE SCENES?
# =============================================================================

print(f"\n{'=' * 55}")
print("  WHAT HAPPENED BEHIND THE SCENES?")
print("=" * 55)

print("""
  In those 5 lines, LlamaIndex automatically:

  1. CHUNKING
     Split each document into nodes (in this case, each doc
     is small enough to be one node)

  2. EMBEDDING
     Sent each chunk to OpenAI's embedding API to get a
     1536-dimensional vector representing its meaning

  3. INDEXING
     Stored the vectors in an in-memory vector store
     for fast similarity search

  4. RETRIEVAL
     When you asked "What is the pricing?", it:
     - Embedded your question into a vector
     - Found the most similar document vectors (cosine similarity)
     - Retrieved the top-k most relevant chunks

  5. SYNTHESIS
     Sent the retrieved chunks + your question to the LLM,
     which generated a grounded answer
""")


# =============================================================================
# TRY MORE QUESTIONS
# =============================================================================

print("=" * 55)
print("  TRY MORE QUESTIONS")
print("=" * 55)

questions = [
    "What is the refund policy?",
    "Is there a free trial?",
    "What kind of support do enterprise customers get?",
]

print()
for q in questions:
    response = engine.query(q)
    print(f"  Q: {q}")
    print(f"  A: {response}\n")


# =============================================================================
# KEY TAKEAWAY
# =============================================================================

print("=" * 55)
print("  KEY TAKEAWAY")
print("=" * 55)

print("""
  LlamaIndex's power is in its simplicity:

    5 lines = Complete RAG system

  Compare to building from scratch:
    - Manual chunking logic
    - Embedding API calls
    - Vector store setup
    - Similarity search implementation
    - Prompt engineering for synthesis
    = 100+ lines of code

  LlamaIndex handles ALL of this with sensible defaults,
  while letting you customize every component when needed.

  Next chapter: Setting up your environment properly!
""")

print("=" * 55)
print("  ✓ Complete! You've built your first RAG system!")
print("=" * 55)
