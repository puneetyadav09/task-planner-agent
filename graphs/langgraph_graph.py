# graphs/langgraph_graph.py

from langgraph.graph import StateGraph, END
from steps.planner import planner_step

# Define the state schema (keys expected in the input/output dictionary)
state_schema = {
    "input": str,
    "output": str
}

def create_planner_graph():
    # Initialize graph with the schema
    graph = StateGraph(state_schema)

    # Add the planner node
    graph.add_node("planner", planner_step)

    # Define entry point and edge to END
    graph.set_entry_point("planner")
    graph.add_edge("planner", END)

    # Compile and return the graph
    return graph.compile()
