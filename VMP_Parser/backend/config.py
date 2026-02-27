"""
config.py - Configuration module for VMP_Parser
Loads environment variables, stores constants, and ensures output directories exist.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Supported languages for translation
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
}

# Output folder path (relative to backend/)
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "output")

# Data folder path
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")

# Abbreviation map file path
ABBREVIATION_MAP_PATH = os.path.join(DATA_FOLDER, "abbreviation_map.json")


def ensure_output_folder():
    """Create the output folder if it doesn't exist."""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# Auto-create output folder on import
ensure_output_folder()
