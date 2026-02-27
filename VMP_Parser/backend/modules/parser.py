"""
parser.py - Prescription text parser module
Expands abbreviations, extracts dosage/frequency/duration using regex,
and returns structured prescription data.
"""

import re
import json
import os

# Load abbreviation map and frequency patterns from JSON
_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

with open(os.path.join(_DATA_DIR, "abbreviation_map.json"), "r") as f:
    _data = json.load(f)

MEDICINE_ABBREVIATIONS = _data.get("medicine_abbreviation", {})
FREQUENCY_PATTERNS = _data.get("frequency_patterns", {})


def expand_abbreviations(text: str) -> str:
    """Replace known medicine abbreviations with full names."""
    words = text.split()
    expanded = []
    for word in words:
        clean_word = word.strip(".,;:()")
        if clean_word in MEDICINE_ABBREVIATIONS:
            expanded.append(MEDICINE_ABBREVIATIONS[clean_word])
        else:
            expanded.append(word)
    return " ".join(expanded)


def extract_dosage(text: str) -> str:
    """Extract dosage patterns like 500mg, 250 mg, 10ml, etc."""
    match = re.search(r"(\d+\.?\d*)\s*(mg|ml|g|mcg|iu|units?)", text, re.IGNORECASE)
    return match.group(0).strip() if match else "Not specified"


def extract_duration(text: str) -> str:
    """Extract duration patterns like '5 days', '2 weeks', '1 month'."""
    match = re.search(
        r"(\d+)\s*(days?|weeks?|months?|d|w|m)\b", text, re.IGNORECASE
    )
    return match.group(0).strip() if match else "Not specified"


def extract_frequency(text: str) -> str:
    """
    Match frequency patterns from the known frequency map.
    Falls back to common abbreviations.
    """
    # Check for numeric patterns like 1-0-1
    for pattern, meaning in FREQUENCY_PATTERNS.items():
        if pattern in text:
            return meaning

    # Fallback: check common abbreviation patterns
    freq_abbrevs = {
        "BD": "Twice daily",
        "OD": "Once daily",
        "TDS": "Three times daily",
        "QID": "Four times daily",
        "HS": "At bedtime",
        "SOS": "When required",
        "PRN": "As needed",
        "STAT": "Immediately",
    }
    for abbr, meaning in freq_abbrevs.items():
        if re.search(rf"\b{abbr}\b", text, re.IGNORECASE):
            return meaning

    return "Not specified"


def parse_prescription(text: str) -> list:
    """
    Parse prescription text into a list of structured dictionaries.
    Each entry contains: medicine, dosage, frequency, duration.
    """
    expanded_text = expand_abbreviations(text)
    lines = expanded_text.strip().split("\n")

    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Try to identify medicine name (first recognizable word)
        medicine = "Unknown"
        words = line.split()
        for word in words:
            clean_word = word.strip(".,;:()")
            # Check if it's a known full medicine name or a remaining abbreviation
            if clean_word in MEDICINE_ABBREVIATIONS.values() or clean_word in MEDICINE_ABBREVIATIONS:
                medicine = MEDICINE_ABBREVIATIONS.get(clean_word, clean_word)
                break
            # Accept capitalized words as potential medicine names
            if clean_word and clean_word[0].isupper() and len(clean_word) > 2:
                medicine = clean_word
                break

        results.append({
            "medicine": medicine,
            "dosage": extract_dosage(line),
            "frequency": extract_frequency(line),
            "duration": extract_duration(line),
        })

    return results
