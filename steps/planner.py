# steps/planner.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

gemini_chat_model = genai.GenerativeModel("gemini-pro")

def planner_step(state: dict) -> dict:
    user_input = state.get("input", "")

    if not user_input:
        return {"input": "", "output": "No input provided."}

    response = gemini_chat_model.generate_content(f"Plan the following:\n\n{user_input}")

    return {"input": user_input, "output": response.text}
