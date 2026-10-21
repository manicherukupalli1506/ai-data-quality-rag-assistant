from pathlib import Path
import streamlit as st

from src.document_loader import load_documents
from src.text_chunker import split_documents
from src.vector_store import create_vector_store
from src.rag_assistant import generate_financial_answer


st.set_page_config(
    page_title="Financial Intelligence AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Document Intelligence Assistant")

st.write(
    "Analyze financial reports using AI, "
    "RAG, LangChain, and ChromaDB."
)

st.divider()

@st.cache_resource
def initialize_rag():
    documents = load_documents()
    chunks = split_documents(documents)
    return create_vector_store(chunks)
    
st.subheader("📂 Upload Financial Documents")

uploaded_file = st.file_uploader(
    "Choose a PDF or TXT financial report",
    type=["pdf", "txt"]
)

if uploaded_file is not None:
    folder = Path("financial_documents")
    folder.mkdir(exist_ok=True)

    file_path = folder / Path(uploaded_file.name).name

    if st.button("Save Uploaded Document"):
        file_path.write_bytes(uploaded_file.getbuffer())

        initialize_rag.clear()

        st.success(
            f"Document '{uploaded_file.name}' uploaded successfully!"
        )





question = st.text_input(
    "Ask a question about the financial report:",
    placeholder="What are NovaTech's major business risks?"
)

if st.button("Analyze Financial Report"):
    if question.strip():
        with st.spinner("AI is analyzing the financial report..."):
            try:
                vector_store = initialize_rag()

                result = generate_financial_answer(
                    vector_store,
                    question
                )

                st.subheader("AI-Generated Answer")
                st.write(result["answer"])

                st.subheader("Source Documents")
                for source in result["sources"]:
                    st.write("📄", source)

            except Exception as error:
                st.error(f"An error occurred: {error}")
    else:
        st.warning("Please enter a question.")