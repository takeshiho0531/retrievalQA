import os
import sys

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def retrieve(query):
    if query == "":
        print("")
        return []
    top_k = 5
    embeddings = OpenAIEmbeddings()

    db = FAISS.load_local("./embed/data_faiss", embeddings)

    docs = db.similarity_search(query, k=int(top_k))
    # print(docs)
    # print(docs[0].metadata['source']) :./data/chap1_10.pdf
    # print(type(docs[0].metadata)) :dict
    # file_path=docs[0].metadata['source']
    # print(os.path.basename(file_path)) :chap1_10.pdf

    basis_file_list = []
    for i in range(top_k):
        file_path = docs[i].metadata["source"]
        file_name = os.path.basename(file_path)
        basis_file_list.append(file_name)
    # print(str(basis_file_list)[1:-1])
    return str(basis_file_list)[1:-1]


if __name__ == "__main__":
    retrieve(sys.argv[1])
