from graphs.langgraph_graph import create_planner_graph

if __name__ == "__main__":
    planner_graph = create_planner_graph()
    planner_graph.invoke("Plan my day based on meetings, tasks and break")
