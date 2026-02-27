"""
llm.py - LLM integration module
Sends prescription text to an LLM (Gemini) for simplified, patient-friendly explanations.
"""

import google.generativeai as genai
from config import GEMINI_API_KEY


def _get_model():
    """Configure and return the Gemini generative model."""
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please add it to your .env file."
        )
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel("gemini-1.5-flash")


def simplify_prescription(text: str) -> str:
    """
    Send prescription text to the LLM and get a simplified explanation.
    The response will:
    - Explain the purpose of each medicine
    - Explain how to take it
    - Use simple, non-medical language
    - Avoid jargon
    """
    prompt = f"""You are a helpful medical assistant. A patient has received the following prescription.
Please explain it in very simple language that anyone can understand.

For each medicine mentioned:
1. What is it used for?
2. How should the patient take it?
3. Any common things to be careful about?

Avoid medical jargon. Use short, clear sentences.

Prescription:
{text}
"""

    try:
        model = _get_model()
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with LLM: {str(e)}"
