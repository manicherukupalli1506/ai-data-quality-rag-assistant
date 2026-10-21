from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for document in documents:
        split_texts = splitter.split_text(document["content"])

        for index, text in enumerate(split_texts):
            chunks.append({
                "filename": document["filename"],
                "chunk_id": index,
                "content": text
            })

    return chunks