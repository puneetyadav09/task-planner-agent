import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphs.langgraph_graph import create_planner_graph

st.title("🧠 Task Planner with Memory - Gemini")

user_input = st.text_area("Enter your day plan:")

if st.button("Generate Plan"):
    planner_graph = create_planner_graph()
    result = planner_graph.invoke({"input": user_input})
    st.subheader("Tasks")
    for task in result.get("tasks", []):
        st.markdown(f"- {task}")
