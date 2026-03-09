# 🔍 Semantic Search

> Search through **internet & networking concepts** using semantic similarity — powered by **Sentence Transformers**, **Qdrant**, **Groq LLM**, **FastAPI**, and **Streamlit**.

![Status](https://img.shields.io/badge/Status-Work_In_Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector_DB-purple)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Usage](#-usage)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)

---

## 📖 About the Project

**Semantic Search** is a question-answering application that lets you ask natural language questions about **internet and networking concepts** — things like DNS, HTTP, TCP/IP, routing, and more — and get accurate, context-grounded answers.

Unlike traditional keyword search, this app understands the *meaning* of your query. So if you ask *"How do websites find each other?"*, it understands you're asking about DNS — even if you never used the word "DNS".

The app works by storing networking concept documents as **vector embeddings** in a local Qdrant database. When you ask a question, it finds the most semantically similar chunks and passes them to a **Groq LLM** to generate a clean, precise answer.

> 🚧 This project is currently a **work in progress**. Core search and Q&A functionality is working. More features and data are being added.

---

## 🧠 How It Works

```
  Your Question
       │
       ▼
┌─────────────────┐
│ all-MiniLM-L6-v2│  ← converts question to a 384-dim vector
│ Embedding Model │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Qdrant      │  ← finds top-3 most similar document chunks
│  (local file)   │     using cosine similarity
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Groq LLM     │  ← receives context + question, generates answer
│llama-3.1-8b-inst│
└────────┬────────┘
         │
         ▼
     Your Answer
```

**Two-phase process:**

**Phase 1 — Ingestion** (run once):
- Read `internet_docs.txt` and split it into paragraphs
- Embed each paragraph using `all-MiniLM-L6-v2`
- Store vectors + text in local Qdrant database

**Phase 2 — Search & Answer** (every query):
- Embed the user's question
- Query Qdrant for the top-3 most relevant paragraphs
- Send those paragraphs + question to Groq LLM
- Return the generated answer to the frontend

---

## ✨ Features

- 🔍 **Semantic search** — finds relevant content by meaning, not just keywords
- 🌐 **Networking knowledge base** — covers DNS, HTTP, TCP/IP, routing, and more
- 🤖 **LLM-powered answers** — Groq generates clean answers from retrieved context
- ⚡ **Fast inference** — Groq's `llama-3.1-8b-instant` is one of the fastest LLMs available
- 🗄️ **Local vector store** — Qdrant runs fully locally, no cloud account needed
- 🖥️ **Simple UI** — clean Streamlit interface, just type and ask
- 🔌 **REST API** — FastAPI backend makes it easy to integrate anywhere
- 🧩 **Modular codebase** — each component (embedding, vector store, LLM) is its own module

---

## 🛠️ Tech Stack

| Layer | Technology | Details |
|---|---|---|
| **Embeddings** | [Sentence Transformers](https://www.sbert.net/) | `all-MiniLM-L6-v2` — 384-dim vectors |
| **Vector Database** | [Qdrant](https://qdrant.tech/) | Local file-based storage (`qdrant_db/`) |
| **LLM** | [Groq](https://groq.com/) | `llama-3.1-8b-instant` — ultra-fast inference |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) | REST API, serves the RAG pipeline |
| **Frontend** | [Streamlit](https://streamlit.io/) | Interactive question-answering UI |
| **Language** | Python 3.10+ | Core language throughout |

---

## 📁 Project Structure

```
Semantic-Search/
│
├── src/
│   ├── embedding.py        # Loads all-MiniLM-L6-v2, returns vectors
│   ├── vector_store.py     # Qdrant client, create_collection(), search()
│   ├── llm.py              # Groq client, generate_response()
│   ├── rag_pipeline.py     # Orchestrates embed → search → generate
│   ├── ingest.py           # One-time script: chunk docs → embed → store
│   ├── main.py             # FastAPI app with / and /ask endpoints
│   └── app.py              # Streamlit frontend
│
├── data/
│   └── internet_docs.txt   # Networking concepts knowledge base
│
├── qdrant_db/              # Local Qdrant vector store (auto-generated)
│
├── .env                    # API keys — never commit this
├── .env.example            # Safe template to share
├── requirements.txt        # All Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com)

---

### 1. Clone the repository

```bash
git clone https://github.com/cookieshop02/Semantic-Search.git
cd Semantic-Search
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and add your Groq API key (see [Environment Variables](#-environment-variables)).

### 5. Ingest documents into Qdrant

This only needs to be run **once** to populate the vector store:

```bash
python src/ingest.py
```

`

### 6. Start the FastAPI backend

```bash
uvicorn src.main:app --reload --port 8000
```

### 7. Start the Streamlit frontend

```bash
streamlit run src/app.py
```

Open `http://localhost:8501` in your browser and start asking! 🎉

---

## 🔐 Environment Variables

Create a `.env` file in the root of the project:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com).

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

Commit this as `.env.example` instead:

```env
GROQ_API_KEY=
```

---

## 📡 API Reference

Base URL: `http://localhost:8000`

---

### `GET /`

Health check.

**Response:**
```json
{ "message": "Hello buddies!" }
```

---

### `POST /ask`

Ask a question against the networking knowledge base.

**Query Parameter:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `question` | `string` | ✅ | Natural language question to ask |

**Example request:**
```bash
curl -X POST "http://localhost:8000/ask?question=How does DNS work?"
```

**Example response:**
```json
{
  "answer": "DNS (Domain Name System) works by translating human-readable domain names like google.com into IP addresses. When you type a URL, your computer queries a DNS resolver, which looks up the domain and returns the corresponding IP address so your browser can connect to the right server."
}
```

---

## 💡 Usage

Once the app is running, open `http://localhost:8501` and try asking questions like:

```
How does DNS work?
What is the difference between TCP and UDP?
What happens during an HTTP request?
How does IP routing work?
What is a subnet mask?
Explain the OSI model.
What is a CDN and how does it work?
```

The app will retrieve the most relevant paragraphs from the knowledge base and generate a clear, grounded answer using Groq.

---

## 🗺️ Roadmap

- [x] Semantic search with Qdrant + Sentence Transformers
- [x] LLM answer generation with Groq
- [x] FastAPI backend
- [x] Streamlit frontend
- [ ] Expand knowledge base with more networking topics
- [ ] Add chat history / conversation memory
- [ ] Show retrieved source chunks in the UI
- [ ] Add support for PDF and DOCX documents
- [ ] Deploy to Streamlit Cloud

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ by <a href="https://github.com/cookieshop02">cookieshop02</a></p>