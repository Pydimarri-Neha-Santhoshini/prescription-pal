"""
translator.py - Translation module
Translates text into supported vernacular languages using googletrans.
Supported: English, Telugu, Hindi.
"""

from googletrans import Translator

_translator = Translator()


def translate_text(text: str, target_language: str = "en") -> str:
    """
    Translate the given text to the target language code.
    Supported codes: 'en' (English), 'te' (Telugu), 'hi' (Hindi).
    """
    if target_language == "en":
        return text  # No translation needed

    try:
        result = _translator.translate(text, dest=target_language)
        return result.text
    except Exception as e:
        return f"Translation error: {str(e)}"
