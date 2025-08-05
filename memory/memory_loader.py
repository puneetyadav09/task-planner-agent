def save_to_memory(vectorstore, content: str):
    vectorstore.add_texts([content])
