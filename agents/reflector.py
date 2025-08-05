from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

def reflect_on_day(notes):
    return llm.predict(f"What went well today? {notes}")
