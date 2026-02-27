"""
utils.py - Utility helper functions
Provides common helpers used across all modules.
"""

import os
import re
import uuid
from datetime import datetime


def clean_text(text: str) -> str:
    """
    Clean raw OCR text by removing extra whitespace,
    non-printable characters, and normalizing line breaks.
    """
    # Remove non-printable characters
    text = re.sub(r"[^\x20-\x7E\n]", "", text)
    # Normalize multiple spaces to single space
    text = re.sub(r"[ \t]+", " ", text)
    # Normalize multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def ensure_folder_exists(folder_path: str):
    """Create a folder if it doesn't already exist."""
    os.makedirs(folder_path, exist_ok=True)


def generate_unique_filename(prefix: str = "output", extension: str = "txt") -> str:
    """
    Generate a unique filename using timestamp and UUID.
    Example: output_20240101_120000_abc123.txt
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    short_id = uuid.uuid4().hex[:6]
    return f"{prefix}_{timestamp}_{short_id}.{extension}"
