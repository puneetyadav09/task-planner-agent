from langgraph.graph import StateGraph, END
from task_planner_types import TaskPlannerState

from agents.task_extractor import extract_tasks
from agents.planner import generate_day_plan
from memory.chroma_db import get_vectorstore
from memory.memory_loader import save_to_memory

vectorstore = get_vectorstore()

def input_node(state):
    return {"user_input": state["user_input"]}

def extract_node(state):
    return {"tasks": extract_tasks(state["user_input"])}

def plan_node(state):
    plan = generate_day_plan(state["tasks"])
    save_to_memory(vectorstore, plan)
    return {"plan": plan}

def create_planner_graph():
    graph = StateGraph(TaskPlannerState)
    graph.add_node("input", input_node)
    graph.add_node("extract", extract_node)
    graph.add_node("plan", plan_node)

    graph.set_entry_point("input")
    graph.add_edge("input", "extract")
    graph.add_edge("extract", "plan")
    graph.set_finish_point("plan")

    return graph.compile()
