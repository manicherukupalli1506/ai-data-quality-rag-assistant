from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks):
    documents = [
        Document(
            page_content=chunk["content"],
            metadata={
                "filename": chunk["filename"],
                "chunk_id": chunk["chunk_id"]
            }
        )
        for chunk in chunks
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="financial_reports",
        persist_directory="./chroma_db"
    )

    return vector_store