"""
ocr.py - Optical Character Recognition module
Handles image preprocessing and text extraction using Tesseract OCR.
"""

import cv2
import pytesseract
from modules.utils import clean_text


def preprocess_image(image_path: str):
    """
    Preprocess the image for better OCR accuracy.
    Steps: grayscale conversion, Gaussian blur, adaptive thresholding.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding for better contrast
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    return thresh


def extract_text(image_path: str) -> str:
    """
    Extract text from a prescription image using Tesseract OCR.
    Returns cleaned text string.
    """
    preprocessed = preprocess_image(image_path)
    raw_text = pytesseract.image_to_string(preprocessed)
    return clean_text(raw_text)
