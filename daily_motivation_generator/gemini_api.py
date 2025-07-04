import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_motivation(mood):
    prompt = f"Give a short, uplifting motivational message for someone who is feeling '{mood}'. Keep it warm and encouraging."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
