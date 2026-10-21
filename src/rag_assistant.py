from langchain_ollama import ChatOllama


def retrieve_financial_context(vector_store, question):
    results = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    sources = list(set(
        document.metadata.get("filename", "Unknown")
        for document in results
    ))

    return {
        "question": question,
        "context": context,
        "sources": sources
    }


def generate_financial_answer(vector_store, question):
    retrieved = retrieve_financial_context(
        vector_store,
        question
    )

    llm = ChatOllama(
        model="qwen2.5:1.5b",
        temperature=0
    )

    prompt = f"""
You are a financial document analysis assistant.

Answer the user's question using only the
financial information provided below.

If the answer is not available in the context,
say "The information is not available in the document."

Financial Context:
{retrieved["context"]}

Question:
{question}

Provide a clear and concise answer.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": retrieved["sources"]
    }