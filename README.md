# 📄 PDF Chatbot using LangChain, FAISS, Hugging Face Embeddings, and Groq

## Overview

This project is a Retrieval-Augmented Generation (RAG) based PDF Chatbot that allows users to upload a PDF document and ask questions about its content in natural language.

The application extracts text from the uploaded PDF, splits it into manageable chunks, converts those chunks into vector embeddings, stores them in a FAISS vector database, retrieves the most relevant information for a user's query, and uses the Llama 3.3 70B model hosted on Groq to generate accurate answers.

---

## Features

* Upload PDF documents
* Automatic PDF text extraction
* Intelligent text chunking with overlap
* Semantic search using FAISS
* Hugging Face sentence embeddings
* Question answering using Groq's Llama 3.3 70B model
* Fast retrieval-augmented generation (RAG) pipeline
* Simple and user-friendly interface

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Frameworks & Libraries

* LangChain
* FAISS
* Hugging Face Embeddings
* Sentence Transformers
* PyPDF
* Groq API

### Language Model

* Llama 3.3 70B Versatile

---

## Project Architecture

```text
PDF Upload
     │
     ▼
PyPDFLoader
     │
     ▼
Document Extraction
     │
     ▼
RecursiveCharacterTextSplitter
     │
     ▼
Document Chunks
     │
     ▼
HuggingFace Embeddings
     │
     ▼
Vector Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Retriever
     │
User Question
     │
     ▼
Similarity Search
     │
     ▼
Top Relevant Chunks
     │
     ▼
Llama 3.3 70B (Groq)
     │
     ▼
Generated Answer
```

---

## How It Works

### 1. PDF Loading

The uploaded PDF is processed using `PyPDFLoader`.

```python
loader = PyPDFLoader(pdf_path)
docs = loader.load()
```

Each page is converted into a LangChain Document object.

---

### 2. Text Chunking

Large documents are divided into smaller chunks for efficient retrieval.

```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

Chunk overlap helps preserve context across chunks.

---

### 3. Embedding Generation

Each chunk is converted into a numerical vector representation using the Hugging Face embedding model.

```python
HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

These embeddings capture the semantic meaning of the text.

---

### 4. Vector Storage

Embeddings are stored in a FAISS vector database.

```python
FAISS.from_documents(
    docs,
    embeddings
)
```

FAISS enables efficient similarity search over document chunks.

---

### 5. Retrieval

When a user asks a question, the query is converted into an embedding and compared against stored vectors.

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k":3}
)
```

The top 3 most relevant chunks are retrieved.

---

### 6. Answer Generation

The retrieved chunks are provided as context to the Groq-hosted Llama model.

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)
```

The model generates a final answer based on the retrieved information.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/pdf-chatbot-rag.git
cd pdf-chatbot-rag
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Obtain your API key from Groq and replace the placeholder value.

---

## Running the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

## Example Usage

1. Launch the application.
2. Upload a PDF document.
3. Wait for indexing to complete.
4. Enter a question related to the document.
5. Receive an AI-generated answer based on the document content.

---

## Sample Questions

```text
What is machine learning?

Summarize chapter 3.

What are the key findings discussed in the document?

Explain the methodology used in the paper.

What conclusions were drawn by the authors?
```

---

## Folder Structure

```text
pdf-chatbot-rag/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
└── uploaded_pdfs/
```

---

## Future Improvements

* Chat history support
* Multiple PDF uploads
* Source citation display
* Conversation memory
* Hybrid search (keyword + vector search)
* Support for DOCX and TXT files
* Cloud deployment

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector databases and semantic search
* Document embeddings
* LangChain pipelines
* LLM integration using Groq
* Building AI-powered document assistants

---

## Acknowledgements

* LangChain
* Hugging Face
* Sentence Transformers
* FAISS
* Groq
* Streamlit

---

## License

This project is intended for educational and learning purposes. Feel free to fork, modify, and extend it for your own projects.
