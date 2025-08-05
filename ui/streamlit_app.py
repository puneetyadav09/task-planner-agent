import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langgraph_graph import create_planner_graph

planner_graph = create_planner_graph()

st.title("🧠 Task Planner with LangGraph")

user_input = st.text_area("Enter your task description")
if st.button("Generate Plan"):
    if user_input.strip():
        state = {"user_input": user_input}
        result = planner_graph.invoke(state)
        st.subheader("📅 Your Day Plan")
        st.write(result["plan"])
