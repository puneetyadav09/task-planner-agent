from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

def get_vectorstore():
    embedding = OllamaEmbeddings(model="mistral")
    vectorstore = Chroma(
        collection_name="planner_memory",
        embedding_function=embedding,
    )
    return vectorstore
