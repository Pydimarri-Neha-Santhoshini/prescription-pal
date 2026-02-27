"""
tts.py - Text-to-Speech module
Generates audio files from text using gTTS (Google Text-to-Speech).
"""

from gtts import gTTS
from config import OUTPUT_FOLDER
from modules.utils import generate_unique_filename


def generate_audio(text: str, language_code: str = "en") -> str:
    """
    Convert text to speech and save as an MP3 file.
    Returns the file path of the generated audio.
    """
    filename = generate_unique_filename(extension="mp3")
    filepath = f"{OUTPUT_FOLDER}/{filename}"

    try:
        tts = gTTS(text=text, lang=language_code, slow=False)
        tts.save(filepath)
        return filepath
    except Exception as e:
        raise RuntimeError(f"TTS generation failed: {str(e)}")
