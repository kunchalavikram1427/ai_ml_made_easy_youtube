# 📖 Common AI/ML Terminology — Part 03

**From AI Agents to RAG & MCP: Building Smarter AI Systems**

> 📺 **Course:** AI ML Foundations | **Author:** Vikram | **Channel:** [AI ML Made Easy](https://www.youtube.com/@aimlmadeeasy)

This is Part 3 of the Common AI/ML Terminology series — and it's the most practical one yet. It covers how to overcome LLM limitations using techniques like **RAG (Retrieval-Augmented Generation)**, the **MCP (Model Context Protocol)**, and how **AI Agents** and **Agentic AI** systems work. These are the building blocks of production AI systems in 2024–2025.

---

## 📑 Table of Contents

- [LLM Limitations](#-llm-limitations)
- [Overcoming LLM Limitations](#-overcoming-llm-limitations)
- [RAG — Retrieval-Augmented Generation](#-rag--retrieval-augmented-generation)
- [Knowledge Bases](#-knowledge-bases)
- [Chunking & Strategies](#-chunking--strategies)
- [Embeddings & Embedding Models](#-embeddings--embedding-models)
- [Cosine Similarity](#-cosine-similarity)
- [Semantic Search](#-semantic-search)
- [Vector Databases](#-vector-databases)
- [RAG Pipeline: Ingestion](#-rag-pipeline-ingestion)
- [RAG Pipeline: Retrieval & Reranking](#-rag-pipeline-retrieval--reranking)
- [Hybrid Search](#-hybrid-search)
- [RAG Limitations](#-rag-limitations)
- [MCP — Model Context Protocol](#-mcp--model-context-protocol)
- [RAG vs MCP](#-rag-vs-mcp)
- [AI Agents](#-ai-agents)
- [Agentic AI](#-agentic-ai)
- [AI Agents vs Agentic AI](#-ai-agents-vs-agentic-ai)
- [Reasoning in AI](#-reasoning-in-ai)
- [Key Takeaways](#-key-takeaways)

---

## 🚧 LLM Limitations

Large Language Models are powerful but have **fundamental limitations** that affect their reliability and usefulness in production systems.

| Limitation | What Goes Wrong | Example |
|---|---|---|
| **Knowledge cutoff** | Can't access information after training date | "What happened in the news yesterday?" → Can't answer |
| **No private data access** | Doesn't know your company's internal docs | "What's our refund policy?" → Generic, not personalized |
| **Hallucinations** | Generates plausible but incorrect information | Cites papers that don't exist |
| **No real-time data** | Can't check current prices, weather, status | "What's AAPL stock price?" → Outdated or made up |
| **No ability to act** | Can only generate text, can't execute actions | Can't actually send emails, update databases, or call APIs |
| **Context window limits** | Can't process an entire codebase or document set at once | Forgets earlier context in long conversations |

> 💡 **Key insight:** LLMs are trained on a static snapshot of the internet. They're like a very smart person who read everything up to a certain date — but hasn't checked the news since, doesn't know your company's internal docs, and can't actually DO anything in the real world.

---

## 🔧 Overcoming LLM Limitations

Several techniques have been developed to make LLMs more reliable, accurate, and capable:

```
┌─────────────────────────────────────────────────────────────────┐
│          Techniques to Overcome LLM Limitations                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Problem: Outdated knowledge / No private data                   │
│  Solution: RAG — Retrieve relevant docs, include as context      │
│                                                                  │
│  Problem: Can't take actions                                     │
│  Solution: Tool use — LLM calls APIs, databases, functions       │
│                                                                  │
│  Problem: N×M integration mess                                   │
│  Solution: MCP — Standard protocol for AI↔tool connections       │
│                                                                  │
│  Problem: Single-step responses only                             │
│  Solution: AI Agents — Multi-step planning and execution         │
│                                                                  │
│  Problem: Needs domain-specific behavior                         │
│  Solution: Fine-tuning — Retrain on specialized data             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 RAG — Retrieval-Augmented Generation

**RAG (Retrieval-Augmented Generation)** is a technique that enhances LLM responses by **retrieving relevant external documents** and including them as context before generating an answer.

```
┌─────────────────────────────────────────────────────────────────┐
│                    RAG — The Core Idea                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Without RAG:                                                    │
│    User: "What's our company's vacation policy?"                 │
│    LLM:  "Most companies offer 2-3 weeks..." (generic guess)    │
│                                                                  │
│  With RAG:                                                       │
│    User: "What's our company's vacation policy?"                 │
│    System: [Retrieves company_handbook.pdf, section 4.2]         │
│    LLM:  "Per section 4.2, you get 20 days PTO plus..."         │
│           (accurate, grounded in your actual documents)          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Why RAG Matters

| Benefit | How It Helps |
|---|---|
| **Reduces hallucinations** | Responses are grounded in actual source documents |
| **Up-to-date information** | Access data beyond the LLM's training cutoff |
| **Private data access** | Connect to proprietary docs without fine-tuning the model |
| **Cost-effective** | Much cheaper than fine-tuning for many use cases |
| **Auditable** | Can cite sources and trace where information came from |

### Where RAG Is Used

RAG is used wherever you need accurate, up-to-date, or private information that a base LLM alone can't reliably provide:
- Internal knowledge bases and company wikis
- Customer support chatbots with product documentation
- Legal research across case law databases
- Medical Q&A grounded in clinical guidelines
- Code documentation search and developer assistants

---

## 🗃️ Knowledge Bases

**Knowledge Bases** are collections of information that an AI system can retrieve and use to answer questions accurately. They serve as the "source of truth" that RAG systems pull from.

**Types of knowledge bases:**

| Source Type | Examples |
|---|---|
| Documents | PDFs, Word docs, wikis, Confluence pages |
| Databases | SQL databases, data warehouses |
| APIs | Real-time data feeds, CRM systems |
| Code repositories | GitHub repos, documentation sites |
| Structured data | CSVs, spreadsheets, knowledge graphs |

> 🎯 **Analogy:** If the LLM is a smart consultant, the knowledge base is the filing cabinet they reference. Without it, they give generic advice. With it, they give accurate answers specific to your organization.

---

## ✂️ Chunking & Strategies

**Chunking** is the process of breaking large documents into smaller, semantically meaningful segments (chunks) for efficient storage, retrieval, and processing.

### Why Chunking Matters

- LLMs have context window limits — entire documents often can't be sent at once
- Smaller chunks enable **more precise retrieval** — only the most relevant section is returned, not the entire 200-page document
- Better chunks = better search results = better LLM answers

### Chunking Strategies

| Strategy | How It Works | Best For |
|---|---|---|
| **Fixed-size** | Split every N characters/tokens (e.g., 500 tokens per chunk) | Simple, predictable, fast |
| **Sentence-based** | Split on sentence boundaries | Preserving complete thoughts |
| **Paragraph-based** | Split on paragraph/section breaks | Well-structured documents |
| **Semantic** | Use AI to identify topic boundaries | Complex documents with mixed topics |
| **Recursive** | Try large chunks first, subdivide if too big | Adapting to varied document structures |
| **Overlapping** | Chunks overlap by N tokens | Avoiding loss of context at boundaries |

> 💡 **Best practice:** Use overlapping chunks (e.g., 500 tokens with 50-token overlap) to avoid cutting important context at chunk boundaries. A fact that spans two chunks would otherwise be lost.

---

## 🧭 Embeddings & Embedding Models

**Embeddings** convert text into numerical vectors that capture semantic meaning — words/sentences with similar meaning have vectors that are close together.

### Embedding Models in RAG

RAG systems use **external embedding models** specifically designed to convert text into searchable vectors:

| Provider | Model | Dimensions |
|---|---|---|
| OpenAI | text-embedding-3-small | 1,536 |
| OpenAI | text-embedding-3-large | 3,072 |
| Hugging Face | all-MiniLM-L6-v2 | 384 |
| Hugging Face | all-mpnet-base-v2 | 768 |
| Cohere | embed-english-v3.0 | 1,024 |

**What embedding models are used for:**
- **Semantic search** — find documents similar in meaning, not just keywords
- **RAG retrieval** — fetch relevant context for LLMs
- **Clustering & classification** — group similar data
- **Recommendation systems** — match users with similar preferences

```
┌──────────────────────────────────────────────────────────────┐
│           How Embeddings Enable Search                         │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Chunk 1: "A car is a fast vehicle"   → [0.82, 0.75, 0.61]  │
│  Chunk 2: "The bus moves quickly"     → [0.81, 0.74, 0.62]  │
│  Chunk 3: "Flowers grow in gardens"   → [0.15, 0.28, 0.91]  │
│                                                               │
│  Query: "Tell me about automobiles"   → [0.83, 0.74, 0.60]  │
│                                                               │
│  Closest match: Chunk 1! (similar vector = similar meaning)   │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 📐 Cosine Similarity

**Cosine similarity** measures how similar two vectors are by calculating the angle between them. It's the most common distance metric used in RAG and semantic search.

| Distance | Meaning | Interpretation |
|---|---|---|
| **~0.0** (close) | Vectors point in the same direction | Very similar meaning |
| **~0.5** | Moderate angle between vectors | Somewhat related |
| **~1.0** (far) | Vectors point in different directions | Unrelated meaning |

**Example:**
- Distance("A car is fast" ↔ "The bus moves quickly") = **0.015** ← Very similar!
- Distance("A car is fast" ↔ "Flowers grow in gardens") = **0.92** ← Very different!

> 🎯 **Analogy:** Imagine two arrows on a map. If they point in the same direction (same meaning), the angle between them is tiny. If they point in completely different directions (different meanings), the angle is large. Cosine similarity measures this angle.

---

## 🔍 Semantic Search

**Semantic search** retrieves results based on **meaning**, not exact keyword matching (like traditional SQL or Ctrl+F search).

| | Keyword Search (Traditional) | Semantic Search (AI-powered) |
|---|---|---|
| **Query:** "automobile issues" | Only finds docs containing "automobile" AND "issues" | Also finds docs about "car problems", "vehicle defects", "engine trouble" |
| **How it works** | Exact string matching | Compares meaning via embeddings |
| **Misses** | Synonyms, paraphrases, related concepts | Nothing semantically relevant |

> 💡 **Key insight:** Semantic search is the core building block of RAG. It's what allows the system to find relevant documents even when the user's question uses completely different wording than the source documents.

---

## 🗄️ Vector Databases

A **vector database** is a specialized database designed to store, index, and search high-dimensional numerical vectors efficiently.

| | Traditional Database | Vector Database |
|---|---|---|
| **Stores** | Rows & columns (structured data) | Vectors + metadata |
| **Retrieves by** | Exact match, SQL queries | Semantic similarity |
| **Search type** | "Find rows WHERE name = 'John'" | "Find documents most similar to this meaning" |
| **Speed** | Fast for exact lookups | Fast for similarity search across millions of vectors |

### What Vector DBs Store

Each entry contains:
- **Vector** — the numerical embedding (e.g., 1,536 dimensions)
- **Metadata** — source file, page number, timestamp, tags
- **Original text** — the actual chunk of text for display

### Popular Vector Databases

| Database | Type | Notable Feature |
|---|---|---|
| **Pinecone** | Managed cloud | Easiest to start, fully managed |
| **Weaviate** | Open source / cloud | Hybrid search built-in |
| **ChromaDB** | Open source | Lightweight, great for prototyping |
| **Qdrant** | Open source / cloud | High performance, Rust-based |
| **pgvector** | PostgreSQL extension | Use your existing Postgres DB |
| **Milvus** | Open source | Scales to billions of vectors |

---

## 📥 RAG Pipeline: Ingestion

The **ingestion pipeline** transforms raw documents into searchable embeddings stored in a vector database. This happens **before** any user asks a question.

```
┌─────────────────────────────────────────────────────────────────┐
│                    RAG Ingestion Pipeline                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Raw Documents                                                   │
│  (PDFs, docs, wikis)                                            │
│       ↓                                                          │
│  [ Parse & Extract Text ]                                        │
│       ↓                                                          │
│  [ Chunk into Segments ]  (e.g., 500 tokens with overlap)        │
│       ↓                                                          │
│  [ Generate Embeddings ]  (via embedding model)                  │
│       ↓                                                          │
│  [ Store Vectors + Metadata ]  (in vector database)              │
│                                                                  │
│  Best practices:                                                 │
│  • Maintain metadata for source attribution                      │
│  • Use consistent chunking strategies                            │
│  • Re-index when source documents change                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 RAG Pipeline: Retrieval & Reranking

When a user asks a question, the **retrieval pipeline** finds the most relevant chunks and feeds them to the LLM:

```
┌─────────────────────────────────────────────────────────────────┐
│              RAG Retrieval & Generation Pipeline                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Question: "What's the vacation policy for remote staff?"   │
│       ↓                                                          │
│  [ Embed the question ] → query vector                           │
│       ↓                                                          │
│  [ Search vector DB ] → top 5-10 most similar chunks             │
│       ↓                                                          │
│  [ Rerank results ] → reorder by deeper relevance scoring        │
│       ↓                                                          │
│  [ Build prompt ] → "Context: {retrieved chunks} Question: ..."  │
│       ↓                                                          │
│  [ LLM generates answer ] → grounded in retrieved documents      │
│       ↓                                                          │
│  Response to user (with source citations)                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Why Reranking?

Initial vector search finds *similar* documents, but similarity ≠ relevance. A **reranker** (a specialized model) looks at the actual question + each retrieved chunk together and scores how well the chunk actually answers the question.

---

## 🔀 Hybrid Search

**Hybrid search** combines keyword-based and semantic approaches for the best of both worlds.

```
┌──────────────────────────────────────────────────────────────┐
│                    Hybrid Search                               │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  User Query: "Python HTTP 404 error handling"                 │
│       ↓                       ↓                               │
│  [Keyword/BM25 Search]    [Semantic Search]                   │
│  Finds exact matches:     Finds meaning-based:                │
│  "404", "HTTP", "Python"  "web error handling",               │
│                           "request exceptions"                 │
│       ↓                       ↓                               │
│  [ Combine & Score Results ]                                  │
│       ↓                                                       │
│  Best of both: precise + conceptual matches                   │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

| Approach | Strength | Weakness |
|---|---|---|
| **Keyword (BM25)** | Exact matches, specific terms, names, codes | Misses synonyms and paraphrases |
| **Semantic** | Understands meaning, handles paraphrases | May miss specific exact terms |
| **Hybrid** | Best of both worlds | Slightly more complex to implement |

> 💡 **BM25 (Best Matching 25)** is a ranking algorithm used in information retrieval to determine how relevant a document is to a search query based on term frequency and document length.

---

## ⚠️ RAG Limitations

RAG isn't a silver bullet. It has its own challenges:

| Limitation | Description |
|---|---|
| **Retrieval quality** | If the wrong chunks are retrieved, the LLM generates wrong answers |
| **Chunking sensitivity** | Poor chunking strategies can split important context across chunks |
| **Embedding quality** | If the embedding model doesn't capture domain-specific meaning well, search fails |
| **Latency** | Adding retrieval adds 100-500ms to response time |
| **Maintenance** | Knowledge base needs to stay current — stale docs = stale answers |
| **Can't take actions** | RAG only provides information — it can't send emails, update records, or call APIs |

---

## 🔌 MCP — Model Context Protocol

### The Problem MCP Solves

Before MCP, every AI application had to build **custom integrations** for each data source and tool. This created an **N×M integration problem** — N applications each needing M custom connectors.

```
┌──────────────────────────────────────────────────────────────┐
│           Before MCP: N×M Integration Problem                  │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  App 1 ──custom──→ Tool A                                     │
│  App 1 ──custom──→ Tool B                                     │
│  App 1 ──custom──→ Tool C                                     │
│  App 2 ──custom──→ Tool A                                     │
│  App 2 ──custom──→ Tool B                                     │
│  App 2 ──custom──→ Tool C                                     │
│  (Every combination needs its own connector = N × M total)    │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│           After MCP: Universal Standard                        │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  App 1 ──┐                    ┌──→ Tool A                     │
│  App 2 ──┤── MCP Protocol ────┤──→ Tool B                     │
│  App 3 ──┘                    └──→ Tool C                     │
│  (One standard protocol connects everything = N + M total)    │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### What is MCP?

**MCP (Model Context Protocol)** is an open standard (created by Anthropic) that provides a universal way for AI applications to connect to external data sources and tools — like a "USB-C for AI."

### MCP Architecture

| Component | Role | Example |
|---|---|---|
| **MCP Host** | The AI application that needs access to tools | Claude Desktop, Cursor, VS Code |
| **MCP Client** | Manages connections to MCP servers | Built into the host application |
| **MCP Server** | Exposes specific tools/data to AI | GitHub MCP server, Slack MCP server, DB server |

### MCP Server Primitives

MCP servers expose **three types of capabilities** that AI models can use:

| Primitive | What It Does | Example |
|---|---|---|
| **Tools** | Actions the AI can execute | Create a GitHub issue, send a Slack message, query a database |
| **Resources** | Data the AI can read | File contents, database records, API responses |
| **Prompts** | Pre-built prompt templates | Specialized workflows, domain-specific instructions |

> 🎯 **Analogy:** MCP is like a universal adapter. Instead of every AI app building a custom plug for every tool (GitHub, Slack, databases, etc.), MCP provides one standard plug that works everywhere. Build one MCP server for GitHub, and every MCP-compatible AI app can use it.

---

## ⚖️ RAG vs MCP

| Dimension | RAG | MCP |
|---|---|---|
| **Purpose** | Retrieve knowledge to inform responses | Connect to tools and take actions |
| **Direction** | Data → AI (pulls information in) | AI → Tools (pushes actions out) |
| **Primary use** | Q&A over documents, knowledge retrieval | Tool use, API calls, system integrations |
| **Real-time data** | Only if knowledge base is kept updated | Yes — live connections to external systems |
| **Actions** | ❌ Cannot execute actions | ✅ Can execute actions (create, update, delete) |
| **Setup** | Embedding pipeline + vector DB | MCP server per tool/data source |

### RAG + MCP Together

The most powerful systems combine both:
- **RAG** provides the knowledge (what does the documentation say?)
- **MCP** provides the actions (now update the ticket, send the notification)

> **Example:** A support agent uses RAG to find the relevant policy, then MCP to update the customer's ticket and send them a refund email — all in one interaction.

---

## 🤖 AI Agents

**AI Agents** are software systems that can perceive input, reason about it, and **take actions** using tools to achieve a specific goal. Unlike traditional AI that only generates text, AI agents interact with external systems (APIs, databases, tools) to perform tasks.

### Key Characteristics

| Characteristic | Description |
|---|---|
| **Autonomy** | Operates with limited human intervention for defined tasks |
| **Perception** | Receives and interprets inputs (user messages, APIs, data) |
| **Reasoning** | Uses LLMs to decide what action to take |
| **Action** | Executes tasks via tools (APIs, queries, code execution) |
| **Memory** | Maintains context within a session (and optionally across sessions) |

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI Agent Architecture                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Input → [ Perceive ] → [ Reason ] → [ Decide ] → [ Act ] │
│                    ↑                                     │       │
│                    └──── Feedback / Observation ──────────┘       │
│                                                                  │
│  Tools available: APIs, databases, search, code execution,       │
│                   file systems, email, calendars, etc.            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**AI Agents are:** Reactive • Goal-Driven • Task-Focused

> **Example — Customer Support Agent:**
> 1. Customer asks: "Where's my order?"
> 2. Agent reasons: I need to look up their order status
> 3. Agent acts: Calls order tracking API
> 4. Agent responds: "Your order #12345 shipped yesterday and arrives Thursday"

---

## 🚀 Agentic AI

**Agentic AI** refers to AI systems designed to act with a **high degree of autonomy**, making complex decisions and executing **multi-step workflows** to achieve a goal using tools, memory, and reasoning.

It represents a shift from reactive chatbots to **proactive systems** that can complete end-to-end tasks like software development, research, and data analysis.

### What Makes AI "Agentic"

| Capability | Description |
|---|---|
| **Goal-directed behavior** | Pursues objectives rather than just responding to prompts |
| **Planning & decomposition** | Breaks complex tasks into smaller steps, executes them sequentially or in parallel |
| **Tool use** | Interacts with external systems (APIs, databases, code execution, web search) |
| **Memory & context** | Maintains state across interactions, uses past information for better decisions |
| **Self-correction** | Evaluates results, iterates, and improves outcomes over time |

**Agentic AI is:** Proactive • Multi-Step • Outcome-Focused

> **Example — Agentic Coding Assistant (like Claude Code):**
> 1. You say: "Fix the failing test in auth.py"
> 2. Agent plans: Read the test → Read the source → Understand the failure → Fix → Verify
> 3. Agent reads the test file and error output
> 4. Agent reads the related source code
> 5. Agent reasons about the root cause
> 6. Agent writes a fix
> 7. Agent runs the tests to verify the fix works
> 8. Agent reports: "Fixed! The issue was a missing null check on line 47"

---

## ⚖️ AI Agents vs Agentic AI

| Dimension | AI Agent | Agentic AI |
|---|---|---|
| **Scope** | Single task or narrow workflow | Complex, multi-step end-to-end workflows |
| **Autonomy** | Moderate — follows defined patterns | High — plans, adapts, self-corrects |
| **Planning** | Minimal — reactive to input | Deep — decomposes goals into sub-tasks |
| **Self-correction** | Limited | Evaluates and iterates on its own work |
| **Example** | "Look up order status" | "Diagnose why revenue dropped, analyze data, and write a report" |

> 💡 **Key distinction:** All agentic systems are agents, but not all agents are truly agentic. A simple lookup bot is an agent. Claude Code autonomously planning, coding, testing, and debugging is agentic.

---

## 🧠 Reasoning in AI

**Reasoning** is the decision-making engine inside AI. It's the step-by-step thinking process AI uses to move from a problem to the best possible action.

It involves:
- Understanding the context
- Analyzing the data
- Drawing conclusions
- Taking the best action

### Types of Reasoning in AI

| Type | Description | Example |
|---|---|---|
| **Chain-of-Thought** | Breaking problems into sequential steps | "Let me work through this step by step..." |
| **Deductive** | Applying general rules to specific cases | "All mammals breathe air. Whales are mammals. Therefore..." |
| **Inductive** | Finding patterns from examples | "These 100 customers churned after X. Pattern suggests..." |
| **Analogical** | Applying knowledge from similar domains | "This is like the routing problem we solved in..." |
| **Abductive** | Finding the best explanation for observations | "The test fails only on Mondays → likely a cron job conflict" |

### Reasoning Models (2024–2025)

A new class of models that **think before answering** — spending compute on reasoning before generating a response:

| Model | Approach | Best For |
|---|---|---|
| OpenAI o1 / o3 | Internal chain-of-thought before answering | Math, logic, coding competitions |
| Claude (extended thinking) | Visible thinking process | Complex analysis, multi-step reasoning |
| Gemini (thinking mode) | Deliberate reasoning | Science, research questions |

> 🎯 **Analogy:** Regular LLMs are like someone who blurts out the first answer that comes to mind. Reasoning models are like someone who pauses, thinks it through on a whiteboard, and then gives you a considered answer. The pause costs more time and compute, but the answer is significantly better for hard problems.

---

## 🎯 Key Takeaways

1. **LLMs have fundamental limits** — knowledge cutoff, hallucinations, no private data, can't take actions
2. **RAG** overcomes knowledge limits by retrieving relevant documents before generating answers
3. **Chunking** strategy directly impacts RAG quality — smaller, overlapping, semantically meaningful chunks work best
4. **Embeddings** turn text into searchable vectors; **vector databases** store and search them efficiently
5. **Semantic search** finds results by meaning, not keywords — the foundation of RAG retrieval
6. **Hybrid search** (keyword + semantic) gives the best retrieval results
7. **MCP** solves the N×M integration problem — one standard protocol for AI↔tool connections
8. **RAG provides knowledge; MCP provides actions** — they complement each other
9. **AI Agents** are task-focused systems that can use tools; **Agentic AI** adds deep planning and self-correction
10. **Reasoning** is what separates modern AI from simple pattern matching — newer models explicitly "think before answering"

---

## 📚 References

- [RAG Paper — "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"](https://arxiv.org/abs/2005.11401)
- [Model Context Protocol — Anthropic](https://modelcontextprotocol.io/)
- [Vector Database Comparison — Superlinked](https://superlinked.com/vector-db-comparison)
- [Building Effective Agents — Anthropic](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Chunking Strategies for RAG — Pinecone](https://www.pinecone.io/learn/chunking-strategies/)

---

> 📺 **Watch the full video on YouTube:** [AI ML Made Easy](https://www.youtube.com/@aimlmadeeasy)
