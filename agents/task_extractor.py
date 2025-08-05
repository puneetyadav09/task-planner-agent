from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

model = ChatOllama(model="mistral")  # or llama3, phi3, etc.

prompt = PromptTemplate(
    input_variables=["input"],
    template="""
You are an expert productivity assistant.
Extract a list of specific actionable tasks from the user's input below.

User Input: {input}

Return tasks as a bullet-point list.
"""
)

chain = LLMChain(llm=model, prompt=prompt)

def extract_tasks(user_input: str):
    response = chain.run(user_input)
    tasks = [line.strip("-• ") for line in response.strip().split("\n") if line.strip()]
    return tasks
