import sys
import re
from glob import glob
from typing import Optional

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PDFMinerLoader
from langchain.text_splitter import (  RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
)
from langchain.vectorstores import FAISS
import tiktoken

import os
os.environ["OPENAI_API_KEY"]="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"


def create_embd_db(parent_regex: str):
    documents_pdf = []

    for path in glob(parent_regex):
        print(path)
        loader: Optional[PDFMinerLoader] = None

        token_num_list=[]

        if re.match(".+\.(pdf)$", path):
            loader = PDFMinerLoader(file_path=path)
            documents_pdf += loader.load()

            data=loader.load()
            print(data)
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10, separator="\n\n")
            text=text_splitter.split_documents(data)
            enc = tiktoken.get_encoding("cl100k_base")
            tokens = enc.encode(str(text))

            if len(tokens)>500:
                token_num_list.append(path)
        print(token_num_list)


    #texts = []
    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
    #texts += text_splitter.split_documents(documents_pdf)

    #embeddings = OpenAIEmbeddings(
        #model="text-embedding-ada-002",
        #chunk_size=1,
    #)
    #db = FAISS.from_documents(texts, embeddings)
    #return db



def main(db_path: str) -> None:
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        chunk_size=1,
    )
    db = create_embd_db(
        parent_regex="./data/msm_data/spec_json/split/統合/*.json",
    )
    db.save_local(db_path)


if __name__ == "__main__":
    #main(
        #db_path="./data/msm_data/spec_json/faiss_index/merged",
    #)
    create_embd_db("./data/*.pdf")