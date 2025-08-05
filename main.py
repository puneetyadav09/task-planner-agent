from langgraph_graph import create_planner_graph
from task_planner_types import TaskPlannerState
from dotenv import load_dotenv
load_dotenv()

planner_graph = create_planner_graph()

if __name__ == "__main__":
    user_input = input("🧠 Enter your task description:\n> ")

    initial_state: TaskPlannerState = {
        "user_input": user_input,
        "tasks": None,
        "plan": None,
    }

    final_state = planner_graph.invoke(initial_state)
    print("\n📅 Final Plan:\n")
    print(final_state["plan"])
