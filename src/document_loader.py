from pathlib import Path
from pypdf import PdfReader


def load_documents(folder_path="financial_documents"):
    documents = []
    folder = Path(folder_path)

    if not folder.exists():
        return documents

    for file_path in sorted(folder.iterdir()):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() == ".txt":
            text = file_path.read_text(encoding="utf-8")

        elif file_path.suffix.lower() == ".pdf":
            reader = PdfReader(str(file_path))

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        else:
            continue

        if text.strip():
            documents.append({
                "filename": file_path.name,
                "content": text
            })

    return documents