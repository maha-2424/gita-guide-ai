import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def detect_mood_ai(question):

    prompt = f"""
Classify the user's message into ONLY ONE of these categories:

Career
Education
Stress
Relationship
General

User:
{question}

Return ONLY the category name.
"""

    response = model.generate_content(prompt)

    return response.text.strip()
    
    
def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "⚠️ AI temporarily unavailable. Please try again."