# 📖 Common AI/ML Terminology — Part 01

**AI & ML Unlocked: The Terms You Need to Know**

> 📺 **Course:** AI ML Foundations | **Author:** Vikram | **Channel:** [AI ML Made Easy](https://www.youtube.com/@aimlmadeeasy)

This is Part 1 of the Common AI/ML Terminology series. It covers the foundational terms you'll encounter everywhere in AI — from what a model actually is, to how LLMs work, hallucinations, fine-tuning, and prompt engineering techniques. These are the building blocks for understanding everything else in AI.

---

## 📑 Table of Contents

- [What is a Model?](#-what-is-a-model)
- [Training Data](#-training-data)
- [Data Split](#-data-split)
- [Model Training](#-model-training)
- [MLOps](#-mlops-machine-learning-operations)
- [Large Language Models (LLMs)](#-large-language-models-llms)
- [Multimodal Models](#-multimodal-models)
- [Knowledge Cutoff](#-knowledge-cutoff-in-llms)
- [Hallucinations](#-hallucinations-in-llms)
- [Fine-Tuning](#-fine-tuning)
- [Prompts & Prompt Engineering](#-prompts--prompt-engineering)
- [Key Takeaways](#-key-takeaways)

---

## 🧩 What is a Model?

In machine learning, a **model** is a mathematical function that learns patterns from data to make predictions or decisions.

Think of it as a **black box** that takes input → produces output.

```
┌─────────────────────────────────────────────────────┐
│                     ML Model                         │
│                                                     │
│   Input ──→ [ Learned Patterns (weights) ] ──→ Output │
│                                                     │
│   "Win a free iPhone!" ──→ [model] ──→ "Spam"      │
│   Photo of a cat       ──→ [model] ──→ "Cat"       │
│   Customer data        ──→ [model] ──→ "$450K"     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Key concepts:**
- A model has many tunable numbers called **parameters** (or **weights**)
- A simple linear model: `y = w₁x₁ + w₂x₂ + b` — where w₁, w₂ are weights and b is a bias (offset)
- **Training** is the process of finding the best values for those numbers
- The more parameters, the more complex patterns the model can learn

> 🎯 **Analogy:** A model is like a student's brain. Before studying (training), it can't answer questions. After studying thousands of examples, it recognizes patterns and can answer new questions it's never seen before.

| Model Size | Parameters | What It Can Do |
|---|---|---|
| Tiny | ~10K | Spam detection, simple classification |
| Medium | ~100M | Sentiment analysis, named entity recognition |
| Large | 7B–70B | General conversation, coding, reasoning |
| Frontier | 400B–1.8T | Complex reasoning, multimodal, expert-level tasks |

---

## 📊 Training Data

**Training data** is the collection of examples used to teach the model. It's the "textbook" that the model learns from.

Training data can be:

| Type | Description | Example |
|---|---|---|
| **Labeled** | Each example has a known correct answer | Email + "spam/not spam" tag |
| **Unlabeled** | Raw data without any answers | Millions of web pages, books, articles |

> 🎯 **Analogy:** Labeled data is like a textbook with an answer key — the student checks their work. Unlabeled data is like reading thousands of books — the student absorbs patterns without explicit answers.

**Quality matters more than quantity.** A model trained on 10,000 high-quality, diverse examples often outperforms one trained on 1 million noisy, repetitive examples. This is sometimes called the "garbage in, garbage out" principle.

---

## ✂️ Data Split

When training a model, you don't use all your data at once. To ensure the model learns patterns rather than just memorizing answers, you split your dataset into distinct subsets:

```
┌─────────────────────────────────────────────────────────────┐
│                    Dataset Split                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐ ┌────────────┐ ┌────────────────┐    │
│  │  Training Set     │ │ Validation │ │   Test Set      │    │
│  │  (~70-80%)        │ │ (~10-15%)  │ │   (~10-15%)     │    │
│  │                   │ │            │ │                  │    │
│  │  Model learns     │ │ Tune &     │ │  Final exam     │    │
│  │  from this        │ │ adjust     │ │  (never seen)   │    │
│  └──────────────────┘ └────────────┘ └────────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

| Set | Purpose | When Used |
|---|---|---|
| **Training** | Model learns patterns from this data | During training |
| **Validation** | Check progress & tune settings (hyperparameters) | During training (after each round) |
| **Test** | Final evaluation on completely unseen data | Only after training is complete |

> 🎯 **Analogy:** Training set = homework (learn from it). Validation set = practice quizzes (check progress). Test set = final exam (the model has never seen these questions).

---

## 🏋️ Model Training

**Model training** is the process of teaching a model by adjusting its parameters (weights) using data to minimize error.

```
┌──────────────────────────────────────────────────────────────┐
│                    Training Process                            │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1. Show the model an example                                 │
│  2. Model makes a prediction                                  │
│  3. Compare prediction to correct answer                      │
│  4. Calculate the error (how wrong it was)                    │
│  5. Adjust weights slightly to reduce that error              │
│  6. Repeat millions/billions of times                         │
│                                                               │
│  After enough iterations: the model's weights encode the      │
│  patterns needed to make accurate predictions                 │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

> 🎯 **Analogy:** Like learning to shoot free throws. Each attempt, you observe where the ball goes wrong, adjust your form slightly, and try again. After 10,000 shots with adjustments, you're accurate — not because you memorized each shot, but because you learned the underlying patterns of a good throw.

---

## ⚙️ MLOps (Machine Learning Operations)

Once a model is trained, how do you deploy, monitor, and maintain it in production? That's where **MLOps** comes in.

**MLOps** is the practice of applying DevOps principles to machine learning — automating the deployment, monitoring, and management of ML models throughout their entire lifecycle.

```
┌─────────────────────────────────────────────────────────────────┐
│                    MLOps Lifecycle                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Data Prep → Training → Evaluation → Deployment → Monitoring    │
│       ↑                                                 │        │
│       └─────────── Retrain when performance drops ──────┘        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**MLOps handles:**
- Automated retraining when data changes or model performance degrades
- Version control for models, data, and experiments
- CI/CD pipelines for model deployment
- Monitoring for data drift, model drift, and performance metrics
- A/B testing between model versions in production

> 🎯 **Analogy:** If building a model is like building a car, MLOps is like running the factory — assembly line automation, quality checks, maintenance schedules, and recall systems when something goes wrong.

**Popular MLOps tools:** MLflow, Kubeflow, Weights & Biases, SageMaker, Vertex AI

---

## 🧠 Large Language Models (LLMs)

**LLMs** are a type of AI model trained on massive amounts of text to understand and generate human language.

**What makes them "large":**

| Dimension | Scale |
|---|---|
| Training data | Hundreds of billions to trillions of words (books, websites, code, articles) |
| Parameters | Billions to trillions of weight numbers |
| Compute | Thousands of GPUs running for weeks or months |
| Cost | $10M–$100M+ for frontier models |

**Examples:** `GPT-4`, `Claude`, `Gemini`, `LLaMA`, `Mistral`

### How LLMs Work — The Core Idea

LLMs are trained to do one thing: **predict the next word (token) in a sequence**. That's it.

But by doing this across trillions of text examples, they develop a deep understanding of language, facts, reasoning, and context.

```
┌───────────────────────────────────────────────────────────────┐
│              How LLM Text Generation Works                      │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│  Your prompt: "What is the capital of France?"                 │
│                                                                │
│  Model predicts next token: "The"                              │
│  Then: "The capital"                                           │
│  Then: "The capital of"                                        │
│  Then: "The capital of France"                                 │
│  Then: "The capital of France is"                              │
│  Then: "The capital of France is Paris"                        │
│  Then: "The capital of France is Paris."  [STOP]               │
│                                                                │
│  Each word is chosen based on what's statistically most        │
│  likely to come next, given everything before it.              │
│                                                                │
└───────────────────────────────────────────────────────────────┘
```

> 💡 **Tokens** are the fundamental units that AI models process — they can be words, parts of words, or characters. "Artificial" might be split into "Art" + "ificial" — two tokens.

---

## 🌐 Multimodal Models

**Multimodal models** are AI models that can work with **multiple types of data** — not just text, but also images, audio, video, and more — within a single unified model.

| Input Type | What the Model Can Do |
|---|---|
| Text | Understand and generate language |
| Images | Describe, analyze, generate, or edit images |
| Audio | Transcribe, understand, generate speech |
| Video | Describe scenes, answer questions about video content |
| Code | Read, write, debug, explain code |

**Examples:** GPT-4o, Gemini Pro, Claude 3.5 (vision), LLaMA 4

> 🎯 **Analogy:** Earlier models were like someone who could only read books. Multimodal models are like someone who can read books, look at photos, listen to music, and watch videos — and discuss all of them.

---

## 📅 Knowledge Cutoff in LLMs

**Knowledge cutoff** defines the latest point in time up to which an LLM has been trained and has information.

**What this means in practice:**
- If a model's cutoff is April 2024, it doesn't know about events after that date
- It can't tell you yesterday's news, recent stock prices, or latest software releases
- This is a fundamental limitation — the model is a "snapshot" of knowledge at training time

**How it's addressed:**
- **Web search integration** — models can search the internet in real-time (ChatGPT, Perplexity)
- **RAG (Retrieval-Augmented Generation)** — connecting models to up-to-date knowledge bases
- **Tool use** — models call APIs to get current data (weather, stocks, databases)

---

## 🌀 Hallucinations in LLMs

**Hallucination** is when an AI model generates incorrect, misleading, or completely made-up information that sounds confident and believable.

**Why it happens:**
- LLMs predict statistically likely text — they don't "know" facts the way a database does
- They prioritize fluent, confident-sounding output over factual accuracy
- If the training data contains errors or gaps, the model fills in with plausible-sounding fiction

**Examples of hallucination:**
- Citing academic papers that don't exist (with realistic-sounding titles and authors)
- Giving confident but wrong answers to math problems
- Inventing historical events that never happened

**How to reduce hallucinations:**
| Strategy | How It Helps |
|---|---|
| RAG | Ground responses in verified source documents |
| System prompts | Tell the model "say I don't know if unsure" |
| Temperature = 0 | Make responses more deterministic, less creative |
| Fact-checking tools | Verify claims against trusted sources |
| Citation requirements | Force the model to reference specific sources |

> ⚠️ **Critical insight:** Hallucinations are not bugs — they're a fundamental property of how LLMs work. They generate text that is *statistically plausible*, not necessarily *true*. Always verify critical information.

---

## 🎯 Fine-Tuning

**Fine-tuning** is the process of adapting a pre-trained model to a specific task or domain by training it on additional, specialized data.

```
┌───────────────────────────────────────────────────────────────┐
│                Fine-Tuning Process                              │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│  Pre-trained Model        Additional Data       Fine-tuned Model│
│  (general knowledge) ──+── (your domain) ──→ (specialized)    │
│                                                                │
│  GPT-4 (general)     + Medical papers     → Medical AI         │
│  LLaMA (general)     + Legal contracts    → Legal AI           │
│  Base model          + Company docs       → Company chatbot    │
│                                                                │
└───────────────────────────────────────────────────────────────┘
```

**When to fine-tune vs. when to use RAG:**

| Approach | Best For | Cost | Effort |
|---|---|---|---|
| **Fine-tuning** | Changing model behavior/style, learning domain-specific language | High (training costs) | Medium-High |
| **RAG** | Adding factual knowledge, keeping info up-to-date | Low-Medium | Medium |
| **Prompt engineering** | Quick adjustments, format changes | Very Low | Low |

> 🎯 **Analogy:** A pre-trained model is like a general doctor. Fine-tuning is like that doctor doing a 3-year residency to become a cardiologist — same foundation, but now specialized in heart-related questions.

---

## 💬 Prompts & Prompt Engineering

A **prompt** is a natural language instruction or question submitted to an AI model to generate a specific response.

**Prompt engineering** is the art and science of structuring prompts to get better, more accurate, and more useful outputs from LLMs.

### Key Prompting Techniques

#### 1. Zero-Shot Prompting

Give the model a task **without any examples**. It relies entirely on its pre-training to understand what you want.

> **Example:** "Summarize this article in 5 bullet points."

**Best for:** Simple, well-defined tasks the model already understands.

---

#### 2. Few-Shot Prompting

Provide a **small number of examples** before asking the real question. This shows the model the pattern, format, and type of answer you want.

> **Example:**
> - Input: "Great movie!" → Sentiment: Positive
> - Input: "It was okay, a bit slow." → Sentiment: Neutral
> - Input: "Waste of time." → Sentiment: ??? (AI fills this in)

**Best for:** Tasks where the format matters, or when the model needs help understanding your specific classification scheme.

---

#### 3. Chain-of-Thought (CoT) Prompting

Encourages the model to **reason step by step** instead of jumping directly to the final answer. Dramatically improves accuracy for logic, math, and multi-step problems.

> **Example:** "Explain how to calculate the ROI of a marketing campaign. Break it down step-by-step."

**Best for:** Math problems, logic puzzles, multi-step analysis, any task requiring reasoning.

---

### Prompting Techniques Comparison

| Technique | Examples Given | When to Use | Accuracy Boost |
|---|---|---|---|
| **Zero-Shot** | None | Simple, familiar tasks | Baseline |
| **Few-Shot** | 2-5 examples | Pattern matching, format-specific tasks | +10-30% |
| **Chain-of-Thought** | Step-by-step reasoning | Math, logic, complex reasoning | +20-50% |

> 💡 **Pro tip:** These techniques stack. You can combine few-shot with chain-of-thought — show examples where the reasoning steps are visible, and the model will follow that pattern.

---

## 🎯 Key Takeaways

1. A **model** is a mathematical function with learned weights that maps inputs to outputs
2. **Training data** quality matters more than quantity — garbage in, garbage out
3. Always **split data** into train/validation/test to prevent memorization
4. **MLOps** brings DevOps discipline to the ML lifecycle (deploy, monitor, retrain)
5. **LLMs** work by predicting the next token — simple objective, emergent intelligence
6. **Multimodal models** handle text, images, audio, and video in one system
7. **Knowledge cutoff** means LLMs are frozen in time — use RAG/tools for current info
8. **Hallucinations** are inherent to LLMs — always verify critical information
9. **Fine-tuning** specializes a general model; **RAG** adds knowledge; **prompting** shapes behavior
10. **Prompt engineering** (zero-shot, few-shot, CoT) dramatically improves output quality

---

## 📚 References

- [Machine Learning Crash Course — Google](https://developers.google.com/machine-learning/crash-course)
- [MLOps Principles — ml-ops.org](https://ml-ops.org/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [What are LLMs? — Anthropic](https://www.anthropic.com/index/what-are-large-language-models)
- [Chain-of-Thought Prompting Paper](https://arxiv.org/abs/2201.11903)

---

> 📺 **Watch the full video on YouTube:** [AI ML Made Easy](https://www.youtube.com/@aimlmadeeasy)
