
# Financial Document Intelligence Assistant

An AI-powered financial document analysis application built with Python, Streamlit, LangChain, Ollama, and ChromaDB.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from financial reports and answer questions using a locally running large language model.

## Features

- Upload PDF and TXT financial documents
- Extract and process document content
- Split documents into searchable text chunks
- Generate semantic embeddings
- Store and retrieve document information using ChromaDB
- Answer financial questions using an Ollama language model
- Display source documents alongside generated answers
- Interactive web interface built with Streamlit

## Technology Stack

- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB
- Hugging Face Sentence Transformers
- PyPDF

## How It Works

1. Upload a financial document.
2. Extract the text from the document.
3. Split the text into smaller chunks.
4. Convert the chunks into vector embeddings.
5. Store the embeddings in ChromaDB.
6. Retrieve relevant information for a user's question.
7. Generate an answer using Ollama.
8. Display the answer and its source documents.

## Project Structure

```text
ai-data-quality-rag-assistant/
├── src/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── vector_store.py
│   ├── rag_assistant.py
│   └── data_quality.py
├── financial_documents/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository and navigate into the project folder.

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama separately and download the language model configured in `src/rag_assistant.py`.

Run the application:

```bash
python -m streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Example Questions

- What was NovaTech's revenue in 2025?
- What were the major business risks faced by NovaTech?
- How did net profit change between 2024 and 2025?
- What are the company's future strategies?

## Sample Financial Insights

Based on the included demonstration report:

- Revenue increased from $120 million to $150 million.
- Net profit increased from $18 million to $24 million.
- Major risks include cybersecurity threats, competition, and increasing cloud costs.

## Future Improvements

- Financial KPI dashboard
- Advanced data quality validation
- Multi-document comparison
- Automated financial summaries
- Cloud deployment

## Project Purpose

This project demonstrates practical skills in Python development, document processing, semantic search, vector databases, retrieval-augmented generation, and building interactive AI applications.
