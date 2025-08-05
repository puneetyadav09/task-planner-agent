from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

model = ChatOllama(model="mistral")

prompt = PromptTemplate(
    input_variables=["tasks"],
    template="""
You are an AI assistant that plans days like a productivity guru.

Given the following tasks, create a well-structured daily plan with timings:

Tasks:
{tasks}

Respond with a detailed hour-by-hour schedule.
"""
)

chain = LLMChain(llm=model, prompt=prompt)

def generate_day_plan(tasks: list[str]):
    task_str = "\n".join(f"- {task}" for task in tasks)
    return chain.run(task_str)
