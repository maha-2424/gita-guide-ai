import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gita_ai(question, verse):

    prompt = f"""
You are GitaGuide AI.

The user asked:

{question}

Relevant Bhagavad Gita Verse:

{verse['verse']}

Verse:

{verse['text']}

Your job:

1. Explain why this verse matches the user's situation.
2. Explain it in very simple English.
3. Give practical guidance.
4. End with ONE motivational sentence.
"""

    response = model.generate_content(prompt)

    return response.text
    
    
def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "⚠️ AI temporarily unavailable. Please try again."