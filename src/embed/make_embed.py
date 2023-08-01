import os
import re
import sys
from glob import glob
from typing import Optional

from langchain.document_loaders import PDFMinerLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


def create_embd_db(parent_regex: str):
    documents_pdf = []

    for path in glob(parent_regex):
        print(path)
        loader: Optional[PDFMinerLoader] = None

        if re.match(".+\.(pdf)$", path):
            loader = PDFMinerLoader(file_path=path)
            documents_pdf += loader.load()

    texts = []
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=10, separator="\n\n"
    )
    texts += text_splitter.split_documents(documents_pdf)

    embeddings = OpenAIEmbeddings()  # type: ignore
    db = FAISS.from_documents(texts, embeddings)
    return db


def main(db_path: str) -> None:
    db = create_embd_db(
        parent_regex="./data/*.pdf",
    )
    db.save_local(db_path)


if __name__ == "__main__":
    main(
        db_path="./data_faiss",
    )
