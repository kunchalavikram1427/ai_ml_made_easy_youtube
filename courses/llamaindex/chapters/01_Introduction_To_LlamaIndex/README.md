# Introduction to LlamaIndex

## Overview

Welcome to the course on **LlamaIndex — Building Intelligent Data Applications with LLMs**! In this chapter, we will explore what LlamaIndex is, why it was created, how it fits into the modern AI ecosystem, and why it remains one of the most important frameworks for building retrieval-augmented generation (RAG) applications in 2026.

By the end of this chapter, you will have a solid understanding of LlamaIndex's purpose, its evolution from a simple RAG library into a full-fledged data framework, and where it excels compared to other tools in the ecosystem. Most importantly, you will understand when and why to use LlamaIndex in your AI projects.

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain what LlamaIndex is and the problem it solves
- Describe the history and evolution of LlamaIndex (from GPT Index to LlamaIndex)
- Understand the core architecture: ingestion → indexing → querying
- Identify real-world use cases where LlamaIndex excels
- Explain why "basic vector RAG" is not enough for production systems
- Understand where LlamaIndex fits in the modern AI stack (vs LangChain, LangGraph)
- Recognize the key components: Documents, Nodes, Indices, Query Engines, Agents
- Describe LlamaIndex's evolution into workflows, agents, and enterprise tooling
- Understand why retrieval quality is the #1 factor in production RAG systems

---

## Prerequisites

- **Basic Python knowledge** — you should be comfortable with Python syntax, functions, classes, and pip
- **General understanding of LLMs** — know what GPT-4, Claude, and other large language models are
- **Basic understanding of APIs** — you've used at least one API (OpenAI, REST, etc.)
- **AI/ML Terminology** — Understand RAG, Vector DBs, Embedding Models, Chunking, MCP, AI Agents, and Agentic AI concepts. Watch this prerequisite video:
  - 📺 [Common AI ML Terms Part 3 | RAG, Vector DBs, Embedding Models, Chunking, MCP, AI Agents, Agentic AI](https://www.youtube.com/watch?v=tQP5dMorMis)
- **No prior LlamaIndex experience required** — this is the starting point!

---

## Detailed Explanation

---

### What is LlamaIndex?

#### The Problem It Solves

Large Language Models (LLMs) like GPT-4, Claude, and Llama are incredibly powerful — they can understand context, generate text, answer questions, and reason about complex topics. But they have a fundamental limitation:

**LLMs only know what they were trained on.**

They don't know about:
- Your company's internal documents
- Your personal notes and knowledge base
- Data that was created after their training cutoff
- Private databases, PDFs, emails, or Slack messages
- Real-time information that changes frequently

This creates a gap between what LLMs *can* do and what they *know*. LlamaIndex bridges this gap.

#### The Definition

**LlamaIndex is a data framework for building context-augmented AI applications.** It provides the tools to:

1. **Ingest** data from any source (PDFs, databases, APIs, websites, etc.)
2. **Structure** that data for efficient retrieval (chunking, embedding, indexing)
3. **Query** the data using natural language through LLMs
4. **Orchestrate** complex workflows involving data retrieval and LLM reasoning

Think of LlamaIndex as the **data layer** for your LLM applications — it handles everything between your raw data and the LLM's response.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        YOUR APPLICATION                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   ┌──────────┐    ┌──────────────┐    ┌──────────────┐              │
│   │  Data     │───▶│  LlamaIndex  │───▶│     LLM      │              │
│   │  Sources  │    │  (Ingestion, │    │  (GPT-4,     │              │
│   │           │    │   Indexing,   │    │   Claude,    │              │
│   │  - PDFs   │    │   Retrieval)  │    │   Llama)     │              │
│   │  - DBs    │    │              │    │              │              │
│   │  - APIs   │    └──────────────┘    └──────────────┘              │
│   │  - Web    │                                                       │
│   └──────────┘                                                       │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

#### A Brief History

| Year | Milestone |
|------|-----------|
| Nov 2022 | Jerry Liu creates "GPT Index" as a side project during the ChatGPT explosion |
| Jan 2023 | Renamed to **LlamaIndex** to avoid trademark issues and broaden scope |
| Mar 2023 | LlamaHub launched — community-driven connector ecosystem |
| Mid 2023 | Raised Series A funding, became a full company |
| Late 2023 | Introduced LlamaParse for advanced document parsing |
| Early 2024 | Added Workflows (event-driven orchestration) |
| Mid 2024 | LlamaCloud launched — managed ingestion and retrieval service |
| 2025 | Matured into enterprise-grade framework with agents, evaluation, and observability |
| 2026 | Established as the de facto standard for retrieval-heavy AI applications |

**Key Insight:** LlamaIndex started as a simple "connect your data to GPT" tool and evolved into a comprehensive data framework with ingestion pipelines, advanced retrieval strategies, agent tooling, evaluation frameworks, and production-grade infrastructure.

---

### Why LlamaIndex Matters in 2026

#### The RAG Evolution

The AI ecosystem has matured significantly. Here's what we've learned:

| Stage | What People Thought | What Actually Works |
|-------|--------------------|--------------------|
| Early 2023 | "Just embed everything into a vector DB" | Basic vector RAG has severe limitations |
| Mid 2023 | "Fine-tune the model on your data" | Expensive, inflexible, doesn't handle updates |
| Late 2023 | "Use better prompts" | Prompts can't fix retrieval quality issues |
| 2024 | "Hybrid search + reranking matters" | Retrieval quality is the #1 production factor |
| 2025-2026 | "Right abstraction for the right problem" | LlamaIndex for retrieval, LangGraph for orchestration |

**The industry realized:** Production RAG is not just "embed and retrieve." It requires:
- Intelligent chunking strategies
- Hybrid search (semantic + keyword)
- Reranking retrieved results
- Metadata filtering
- Multi-source retrieval
- Query understanding and routing
- Evaluation and observability

**LlamaIndex excels at ALL of these.**

#### Where LlamaIndex Excels

LlamaIndex is the strongest choice for:

| Use Case | Why LlamaIndex Wins |
|----------|-------------------|
| **Document Q&A** | Best-in-class ingestion and retrieval pipelines |
| **Enterprise Search** | Multi-source connectors, metadata filtering, access control |
| **PDF Processing** | LlamaParse handles complex layouts, tables, images |
| **Knowledge Bases** | Scalable indexing with production vector stores |
| **Retrieval-heavy Copilots** | Optimized retrieval with reranking and hybrid search |
| **Structured + Unstructured Data** | Text-to-SQL + vector search in one framework |
| **Fast RAG Prototypes** | Go from data to working system in < 10 lines of code |
| **Local/Private RAG** | Works with local LLMs (Ollama, vLLM) and local vector DBs |

#### The Modern AI Stack

In 2026, the production AI stack typically looks like this:

```
┌─────────────────────────────────────────────────────┐
│                  Application Layer                    │
│        (Your app, chatbot, copilot, agent)           │
├─────────────────────────────────────────────────────┤
│              Orchestration Layer                      │
│     (LangGraph, CrewAI, custom agent loops)          │
├─────────────────────────────────────────────────────┤
│               Retrieval / Data Layer                 │
│     (LlamaIndex — ingestion, indexing, querying)     │
├─────────────────────────────────────────────────────┤
│                  LLM Provider                        │
│    (OpenAI, Anthropic, local via Ollama/vLLM)        │
├─────────────────────────────────────────────────────┤
│                  Data Storage                        │
│  (Pinecone, Weaviate, Qdrant, ChromaDB, pgvector)   │
└─────────────────────────────────────────────────────┘
```

**The practical combo used by many teams:**
- **LlamaIndex** for the retrieval + data pipeline
- **LangGraph** for complex agent orchestration (if needed)
- **Simple Python** for straightforward workflows

---

### Core Architecture: The Three-Stage Pipeline

LlamaIndex follows a clean three-stage architecture:

#### Stage 1: Ingestion

Loading data from any source and preparing it for indexing.

```python
from llama_index.core import SimpleDirectoryReader

# Load documents from a folder
documents = SimpleDirectoryReader("./data").load_data()

# Each document has: text content + metadata (filename, date, etc.)
print(f"Loaded {len(documents)} documents")
```

**What happens:**
- Data connectors (readers) load raw data from files, databases, APIs
- Documents are created with text + metadata
- Documents are split into smaller chunks called **Nodes**
- Each Node gets an embedding (vector representation)

#### Stage 2: Indexing

Organizing data for efficient retrieval.

```python
from llama_index.core import VectorStoreIndex

# Create an index from documents
index = VectorStoreIndex.from_documents(documents)

# Behind the scenes:
# 1. Documents → split into Nodes
# 2. Nodes → embedded using an embedding model
# 3. Embeddings → stored in a vector store
```

**What happens:**
- Nodes are embedded using a model (OpenAI, local, etc.)
- Embeddings are stored in a vector store (in-memory, Pinecone, Qdrant, etc.)
- Index metadata is maintained for efficient lookups

#### Stage 3: Querying

Asking questions and getting grounded answers.

```python
# Create a query engine from the index
query_engine = index.as_query_engine()

# Ask a question
response = query_engine.query("What is the company's refund policy?")
print(response)
```

**What happens:**
1. User's question is embedded using the same embedding model
2. Similar Nodes are retrieved from the vector store
3. Retrieved Nodes (context) + user's question are sent to the LLM
4. LLM generates a grounded response based on the retrieved context

---

### Key Components Overview

| Component | Purpose | Analogy |
|-----------|---------|---------|
| **Document** | Raw data loaded from a source | A page in a book |
| **Node** | A chunk of a Document with metadata | A paragraph or section |
| **Index** | Organized collection of Nodes for retrieval | A library's catalog system |
| **Embedding** | Vector representation of text | A fingerprint of meaning |
| **Query Engine** | Stateless Q&A interface | A librarian answering a single question |
| **Chat Engine** | Stateful conversational interface | A librarian remembering your conversation |
| **Retriever** | Fetches relevant Nodes from an index | The search algorithm |
| **Response Synthesizer** | Generates response from retrieved context | The answer composer |
| **Agent** | Autonomous LLM that can use tools and reason | A research assistant |

---

### What Changed Recently (2024-2026)

LlamaIndex has evolved significantly:

| Feature | Description |
|---------|-------------|
| **Workflows** | Event-driven orchestration for complex pipelines (alternative to agents for deterministic flows) |
| **LlamaParse** | Advanced document parsing that handles tables, images, and complex layouts |
| **LlamaCloud** | Managed ingestion and retrieval service for enterprise |
| **Stronger Async** | Full async support throughout the framework for production scalability |
| **Better Observability** | Built-in tracing, callbacks, and integration with observability tools |
| **Agent Tooling** | More sophisticated agent patterns including CodeAct agents |
| **Evaluation Framework** | Tools to measure retrieval quality, answer correctness, and faithfulness |
| **Property Graph Index** | Knowledge graph-based indexing for relationship-rich data |
| **Ingestion Pipelines** | Declarative, reproducible data processing workflows |

---

### Why "Basic Vector RAG" Is Not Enough

Many beginners think RAG is simple:
1. Embed documents
2. Store in vector DB
3. Retrieve similar chunks
4. Send to LLM

In reality, this "naive RAG" approach fails in production because:

| Problem | Description | LlamaIndex Solution |
|---------|-------------|-------------------|
| **Poor chunking** | Fixed-size chunks split sentences and context | Sentence splitter, semantic chunking |
| **Irrelevant retrieval** | Top-k results aren't always the best | Reranking, hybrid search |
| **Missing context** | Retrieved chunk lacks surrounding info | Parent-child nodes, window retrieval |
| **No metadata filtering** | Can't filter by date, source, category | Metadata filters on query |
| **Single data source** | Real apps need multiple sources | Multi-index routing, composable indices |
| **No evaluation** | Can't measure if answers are correct | Built-in eval framework |
| **Hallucination** | LLM makes up information | Citation tracking, faithfulness checks |
| **Scale issues** | Doesn't work with millions of documents | Production vector stores, ingestion pipelines |

**This is exactly why LlamaIndex exists** — it provides solutions for all of these production challenges.

---

### LlamaIndex vs The Alternatives (Quick Overview)

| Framework | Primary Strength | Best For |
|-----------|-----------------|----------|
| **LlamaIndex** | Data ingestion + retrieval | RAG, document Q&A, enterprise search |
| **LangChain** | General LLM orchestration | Chains, basic agents, prototyping |
| **LangGraph** | Stateful agent orchestration | Complex multi-agent systems, approval workflows |
| **Haystack** | Production NLP pipelines | Search engines, enterprise NLP |
| **Semantic Kernel** | Microsoft ecosystem | .NET/C# AI applications |
| **Custom Code** | Full control | Simple, narrow use cases |

**The mental model:**

```
Need retrieval/data?  → LlamaIndex
Need orchestration?   → LangGraph
Need both?            → LlamaIndex (retrieval) + LangGraph (orchestration)
Need simple RAG?      → LlamaIndex alone (no orchestration needed)
```

---

### Real-World Production Use Cases

#### 1. Enterprise Knowledge Base

```
Company Docs (Confluence, Google Drive, SharePoint)
         │
         ▼
    LlamaIndex Ingestion Pipeline
    (connectors, chunking, embedding)
         │
         ▼
    Vector Store (Pinecone/Qdrant)
         │
         ▼
    Query Engine with Metadata Filtering
    (department, date, access level)
         │
         ▼
    Employee Chatbot / Copilot
```

#### 2. PDF Research Assistant

```
Research Papers (100s of PDFs)
         │
         ▼
    LlamaParse (tables, figures, equations)
         │
         ▼
    Hierarchical Indexing
    (paper → section → paragraph)
         │
         ▼
    Multi-document Q&A with Citations
```

#### 3. Customer Support Bot

```
Product Docs + FAQ + Support Tickets
         │
         ▼
    Multi-Source Index with Routing
         │
         ▼
    Router Query Engine
    (routes to relevant index based on question type)
         │
         ▼
    Response with Source Attribution
```

#### 4. Local Private Knowledge Base

```
Personal Notes + Local PDFs + Bookmarks
         │
         ▼
    Local Embedding (sentence-transformers)
         │
         ▼
    Local Vector Store (ChromaDB)
         │
         ▼
    Local LLM (Ollama - Llama 3, Mistral)
         │
         ▼
    100% Private, No Cloud Required
```

---

### Course Roadmap

Here is what you will learn across all chapters in this course:

| Chapter | Topic | Focus |
|---------|-------|-------|
| 01 | **Introduction to LlamaIndex** (You are here!) | What, why, when |
| 02 | Setup and Environment | Installation, API keys, first program |
| 03 | Core Concepts: Documents, Nodes, Indices | The building blocks |
| 04 | Data Ingestion and Connectors | Loading data from any source |
| 05 | Embeddings and Vector Stores | How semantic search works |
| 06 | Querying and Retrieval | Query engines, retrievers, response synthesis |
| 07 | Advanced RAG Techniques | Reranking, hybrid search, metadata filtering |
| 08 | Agents and Tools | Autonomous LLM agents with tool use |
| 09 | Structured Data and Text-to-SQL | Querying databases with natural language |
| 10 | Evaluation and Observability | Measuring and improving quality |
| 11 | Production Deployment | Scaling, caching, async, best practices |
| 12 | LlamaIndex vs LangChain and Ecosystem | Choosing the right tool |

**By the end of this course, you will be able to:**
- Build production-grade RAG applications
- Ingest data from any source (PDFs, databases, APIs, web)
- Implement advanced retrieval strategies (hybrid search, reranking)
- Build conversational agents with tool use
- Query structured and unstructured data with natural language
- Evaluate and improve retrieval quality
- Deploy LlamaIndex applications in production
- Choose the right framework for your specific use case

---

## Running This Chapter

This chapter has 2 Python files you can run directly:

| # | File | What It Does |
|---|------|--------------|
| 1 | `01_what_is_llamaindex.py` | Prints an overview of LlamaIndex — what it is, core concepts, and where it fits in the AI ecosystem |
| 2 | `02_five_line_rag.py` | Builds a complete RAG app in 5 lines — loads sample docs, creates an index, and queries it |

### How to Run

```bash
# Navigate to this chapter
cd courses/llamaindex/chapters/01_Introduction_To_LlamaIndex/

# Run the first file (no API key needed — informational only)
python3 01_what_is_llamaindex.py

# Run the second file (requires OPENAI_API_KEY in .env)
python3 02_five_line_rag.py
```

### Requirements

```bash
pip install llama-index python-dotenv
```

You also need an `.env` file with your OpenAI API key (for `02_five_line_rag.py`):

```bash
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

> **Tip:** If you want to run without an API key (free, local), see Chapter 02 which covers Ollama setup.

---

## Code Examples

### Example 1: The Simplest LlamaIndex App (5 Lines)

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load documents from a folder
documents = SimpleDirectoryReader("./data").load_data()

# Create an index
index = VectorStoreIndex.from_documents(documents)

# Query the index
query_engine = index.as_query_engine()
response = query_engine.query("What is the main topic of these documents?")
print(response)
```

**Output:**
```
The documents primarily discuss [content-specific answer based on your data]...
```

### Example 2: Understanding the Pipeline

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

# Step 1: Load data
documents = SimpleDirectoryReader("./data").load_data()
print(f"Loaded {len(documents)} documents")

# Step 2: Parse into nodes
parser = SentenceSplitter(chunk_size=256, chunk_overlap=20)
nodes = parser.get_nodes_from_documents(documents)
print(f"Created {len(nodes)} nodes")

# Step 3: Build index
index = VectorStoreIndex(nodes)

# Step 4: Query
query_engine = index.as_query_engine(similarity_top_k=3)
response = query_engine.query("Summarize the key points")
print(response)

# You can also see which nodes were retrieved
print("\n--- Sources ---")
for source_node in response.source_nodes:
    print(f"Score: {source_node.score:.4f}")
    print(f"Text: {source_node.text[:100]}...")
    print()
```

---

## Exercises

### Exercise 1: Conceptual Understanding (Beginner)

**Task:** Answer the following questions in your own words:

1. What problem does LlamaIndex solve that LLMs alone cannot?
2. What are the three stages of the LlamaIndex pipeline?
3. What is the difference between a Document and a Node?
4. Why is "naive RAG" (just embedding and retrieving) not enough for production?
5. When would you choose LlamaIndex over LangChain?

<details>
<summary>💡 Click to reveal answers</summary>

1. **LLMs only know what they were trained on.** They cannot access your private data — company docs, databases, PDFs, emails, or real-time information. LlamaIndex bridges this gap by ingesting your private data, indexing it for efficient retrieval, and providing relevant context to the LLM at query time so it can answer questions about YOUR data.

2. **Ingestion → Indexing → Querying.**
   - *Ingestion:* Load data from any source (PDFs, APIs, databases) into Documents
   - *Indexing:* Split Documents into Nodes, embed them, and store in a vector store
   - *Querying:* Embed the user's question, retrieve similar Nodes, and send them as context to the LLM for response generation

3. **A Document is the raw data loaded from a source** (e.g., an entire PDF file or web page). **A Node is a smaller chunk** of a Document (e.g., a paragraph or section). Documents are split into Nodes because LLMs have context limits and retrieval is more precise with smaller, focused chunks. Nodes maintain a relationship back to their parent Document and can carry metadata.

4. **Naive RAG fails in production because:**
   - Fixed-size chunks break sentences and lose context
   - Top-k vector similarity doesn't always return the most relevant results (needs reranking)
   - No metadata filtering (can't filter by date, source, department)
   - Single embedding model misses keyword matches (needs hybrid search)
   - No way to measure if answers are correct (needs evaluation)
   - Doesn't scale well to millions of documents without production vector stores and ingestion pipelines

5. **Choose LlamaIndex when your app is data-centric** — document Q&A, enterprise search, PDF processing, knowledge bases, retrieval-heavy copilots. Choose LangChain when you need general LLM orchestration (chaining calls, broad tool integrations) without complex retrieval needs. Choose LangGraph for stateful multi-agent systems with conditional logic. In practice, many teams use LlamaIndex for retrieval + LangGraph for agent orchestration together.

</details>

---

### Exercise 2: Explore the Ecosystem (Intermediate)

**Task:** Research and answer:

1. Visit [https://docs.llamaindex.ai](https://docs.llamaindex.ai) — What are the main sections of the documentation?
2. Visit [https://llamahub.ai](https://llamahub.ai) — Find 3 data connectors that interest you and describe what they do.
3. What is LlamaParse? When would you use it vs SimpleDirectoryReader?
4. What is LlamaCloud? How does it differ from the open-source library?
5. Find a real company that uses LlamaIndex in production. What do they use it for?

<details>
<summary>💡 Click to reveal answers</summary>

1. **Main documentation sections:**
   - *Getting Started* — Installation, starter tutorial, core concepts
   - *Use Cases* — RAG, chatbots, agents, structured extraction, text-to-SQL, multimodal
   - *Components* — Data connectors, indexes, query engines, chat engines, agents, workflows
   - *Integrations* — LLMs (70+), embeddings (50+), vector stores (80+), callbacks
   - *Advanced* — Evaluation, observability, production deployment, optimization

2. **Example connectors from LlamaHub:**
   - *NotionReader* — Loads pages and databases from Notion workspaces via API token
   - *SlackReader* — Ingests messages and threads from Slack channels for searchable knowledge
   - *DatabaseReader* — Connects to SQL databases (PostgreSQL, MySQL, etc.) and loads query results as documents

3. **LlamaParse** is a managed document parsing service that uses vision-language models to extract text from complex PDFs with tables, charts, images, and nested layouts. Use it when your documents have complex formatting that SimpleDirectoryReader (which uses basic text extraction) would miss or garble. SimpleDirectoryReader is fine for plain text, simple PDFs, and markdown files.

4. **LlamaCloud** is a managed service from the same team that offers:
   - LlamaParse (document parsing)
   - LlamaExtract (schema-based structured extraction)
   - Managed indexing pipelines (auto-sync from SharePoint, Google Drive, S3 → vector DB)
   
   The **open-source library** gives you full control but you manage infrastructure yourself. LlamaCloud handles parsing, embedding, indexing, and syncing as a managed service. Same API patterns — no vendor lock-in.

5. **Example:** Uber uses LlamaIndex-based RAG systems for internal knowledge management, enabling employees to query across engineering documentation, runbooks, and incident reports. Other examples include financial firms using it for SEC filing analysis (the official "SEC Insights" demo app) and healthcare companies for medical literature search.

</details>

---

### Exercise 3: Architecture Thinking (Advanced)

**Task:** For each scenario, describe how you would architect the solution using LlamaIndex:

1. **Scenario:** A law firm wants to search across 50,000 legal contracts to answer questions about specific clauses.
   - What connector would you use?
   - What chunking strategy?
   - What index type?
   - How would you handle metadata?

2. **Scenario:** A startup wants to build a customer support bot that can answer questions from their docs AND check order status from a database.
   - How would you combine structured and unstructured data?
   - What query routing strategy would you use?

3. **Scenario:** A researcher wants to build a private knowledge base using only local tools (no cloud, no API keys).
   - What LLM would you use?
   - What embedding model?
   - What vector store?
   - How would you run everything locally?

<details>
<summary>💡 Click to reveal answers</summary>

**1. Law Firm — 50,000 Legal Contracts:**

- **Connector:** LlamaParse for complex PDF contracts (handles tables, headers, clause numbering) + SimpleDirectoryReader for simple text contracts
- **Chunking:** SentenceSplitter with larger chunk_size (1024 tokens) to keep full clauses intact, with chunk_overlap (200) to preserve cross-boundary context. Consider semantic chunking to split on topic changes rather than fixed sizes.
- **Index type:** VectorStoreIndex backed by a production vector store (Qdrant or Pinecone) for scalability at 50K documents
- **Metadata:** Extract and attach: contract_date, parties_involved, contract_type (NDA, employment, vendor), jurisdiction, expiry_date. Use metadata filters at query time: "Find non-compete clauses in vendor contracts from 2024"

**2. Startup — Support Bot (Docs + Database):**

- **Combining structured and unstructured:**
  - Create a VectorStoreIndex over product docs, FAQ, and support articles (unstructured)
  - Create a NLSQLTableQueryEngine connected to the orders database (structured)
  - Wrap both as tools available to a RouterQueryEngine or an Agent
- **Query routing:** Use a RouterQueryEngine with LLMSingleSelector:
  - Route "How do I reset my password?" → docs VectorStoreIndex
  - Route "What's the status of order #12345?" → SQL query engine
  - Route complex questions to an Agent that can use both tools and combine results

**3. Researcher — Fully Local/Private Knowledge Base:**

- **LLM:** Ollama running Llama 3.2 (8B) or Mistral 7B locally. Install: `ollama pull llama3.2`
- **Embedding model:** `llama-index-embeddings-ollama` with `nomic-embed-text` or `llama-index-embeddings-huggingface` with `BAAI/bge-small-en-v1.5` (runs on CPU)
- **Vector store:** ChromaDB (local, file-based, no server needed) or simple in-memory with `persist_dir` for disk persistence
- **Running locally:**
  ```python
  from llama_index.core import Settings
  from llama_index.llms.ollama import Ollama
  from llama_index.embeddings.ollama import OllamaEmbedding
  
  Settings.llm = Ollama(model="llama3.2", request_timeout=120)
  Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
  ```
  Total cost: $0. No data leaves the machine. Works offline after initial model download.

</details>

---

## Key Takeaways

1. **LlamaIndex is the data layer** for LLM applications — it connects your data to LLMs
2. **Three-stage pipeline** — Ingestion → Indexing → Querying
3. **Production RAG requires more** than basic vector search — chunking, reranking, metadata, evaluation all matter
4. **LlamaIndex excels at retrieval** — document Q&A, enterprise search, PDF processing, hybrid data
5. **Use LlamaIndex for data, LangGraph for orchestration** — they complement each other
6. **The framework has matured significantly** — workflows, agents, eval, observability, enterprise features
7. **Still very relevant in 2026** — retrieval quality is the #1 factor in production AI systems
8. **Works with any LLM** — OpenAI, Anthropic, local models (Ollama, vLLM), and more

---

## Resources & References

### Official Resources
- Official Docs: https://developers.llamaindex.ai
- GitHub: https://github.com/run-llama/llama_index
- LlamaHub Connectors: https://llamahub.ai
- LlamaIndex Blog: https://www.llamaindex.ai/blog

### DeepLearning.AI Short Courses (Free, Official Partnership)
- [Building Agentic RAG with LlamaIndex](https://deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex)
- [Event-Driven Agentic Document Workflows](https://deeplearning.ai/short-courses/event-driven-agentic-document-workflows)
- [Building and Evaluating Advanced RAG](https://deeplearning.ai/short-courses/building-evaluating-advanced-rag)
- [JavaScript RAG Web Apps](https://deeplearning.ai/short-courses/javascript-rag-web-apps-with-llamaindex)

### Community & Learning
- LlamaIndex YouTube Channel: https://www.youtube.com/@LlamaIndex
- LlamaIndex Examples: https://docs.llamaindex.ai/en/stable/examples/

### Tools & Integrations
- OpenAI Platform: https://platform.openai.com/
- Anthropic Console: https://console.anthropic.com/
- Ollama (Local LLMs): https://ollama.com/
- ChromaDB: https://www.trychroma.com/
- Pinecone: https://www.pinecone.io/
- Qdrant: https://qdrant.tech/

---
