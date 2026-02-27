"""
ocr.py - Optical Character Recognition module
Uses Gemini Vision API for text extraction from prescription images.
"""

import os
from PIL import Image
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Configure Gemini client once
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", ""))

EXTRACTION_PROMPT = """You are an expert medical prescription reader.

Carefully read the prescription image.
Extract all visible text exactly as written.

Rules:
- Preserve medicine names
- Preserve dosage values
- Preserve frequency patterns (like 1-0-1, BD, OD, TDS)
- Preserve duration (like 5 days, x7d)
- Do NOT explain
- Do NOT summarize
- Return only the extracted text"""


def extract_text(image_path: str) -> str:
    """
    Extract text from a prescription image using Gemini Vision API.
    Returns cleaned text string.
    """
    try:
        image = Image.open(image_path)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[EXTRACTION_PROMPT, image],
        )
        return response.text.strip() if response.text else ""
    except Exception as e:
        print(f"[OCR Error] Failed to extract text: {e}")
        return ""
