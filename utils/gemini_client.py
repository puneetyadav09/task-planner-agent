import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from environment
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Configure Gemini with the API key
genai.configure(api_key=api_key)

# Instantiate the model
gemini_chat_model = genai.GenerativeModel("gemini-pro")
