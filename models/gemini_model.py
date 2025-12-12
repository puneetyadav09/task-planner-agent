import os
from states.task_planner_state import TaskPlannerState
from google.generativeai import configure, GenerativeModel

configure(api_key=os.getenv("GEMINI_API_KEY"))

model = GenerativeModel("gemini-pro")

def generate_tasks(state: TaskPlannerState) -> TaskPlannerState:
    prompt = f"Generate a task list based on the following input: {state['input']}"
    response = model.generate_content(prompt)
    return {
        **state,
        "tasks": response.text.split("\n"),
        "metadata": {"model": "gemini-pro"}
    }
