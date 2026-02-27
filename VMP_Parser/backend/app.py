"""
app.py - Streamlit main application for VMP_Parser
Vernacular Medical Prescription Parser: Upload a prescription image,
extract text via OCR, parse medicines, simplify with LLM, translate, and listen.
"""

import streamlit as st
import tempfile
import os
from PIL import Image

# Module imports
from modules.ocr import extract_text
from modules.parser import parse_prescription
from modules.llm import simplify_prescription
from modules.translator import translate_text
from modules.tts import generate_audio
from config import SUPPORTED_LANGUAGES

# --- Page Config ---
st.set_page_config(
    page_title="VMP Parser - Prescription Reader",
    page_icon="💊",
    layout="centered",
)

# --- Title & Description ---
st.title("💊 Vernacular Medical Prescription Parser")
st.markdown(
    "Upload a handwritten or printed prescription image. "
    "This tool will read it, explain the medicines in simple language, "
    "and translate it into your preferred language with audio playback."
)
st.divider()

# --- File Upload ---
uploaded_file = st.file_uploader(
    "Upload Prescription Image", type=["png", "jpg", "jpeg", "bmp", "tiff"]
)

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription", use_column_width=True)

    # Save to a temp file for OpenCV/Tesseract processing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)
        temp_path = tmp.name

    # --- Step 1: OCR ---
    st.subheader("📝 Step 1: Extracted Text (OCR)")
    with st.spinner("Extracting text from image..."):
        extracted_text = extract_text(temp_path)

    if extracted_text:
        st.text_area("Raw Extracted Text", extracted_text, height=150)
    else:
        st.warning("No text could be extracted. Please try a clearer image.")
        st.stop()

    # --- Step 2: Parse ---
    st.subheader("💉 Step 2: Parsed Prescription Data")
    with st.spinner("Parsing prescription..."):
        parsed_data = parse_prescription(extracted_text)

    if parsed_data:
        for i, entry in enumerate(parsed_data, 1):
            st.markdown(f"**Medicine {i}:**")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Medicine", entry["medicine"])
            col2.metric("Dosage", entry["dosage"])
            col3.metric("Frequency", entry["frequency"][:20])
            col4.metric("Duration", entry["duration"])
    else:
        st.info("Could not parse structured data from the text.")

    # --- Step 3: LLM Simplification ---
    st.subheader("🧠 Step 3: Simplified Explanation")
    if st.button("Simplify with AI", type="primary"):
        with st.spinner("Asking AI to simplify..."):
            simplified = simplify_prescription(extracted_text)
        st.session_state["simplified"] = simplified

    if "simplified" in st.session_state:
        st.markdown(st.session_state["simplified"])

        # --- Step 4: Translation ---
        st.subheader("🌐 Step 4: Translate")
        selected_lang = st.selectbox(
            "Choose language",
            options=list(SUPPORTED_LANGUAGES.keys()),
        )
        lang_code = SUPPORTED_LANGUAGES[selected_lang]

        if st.button("Translate"):
            with st.spinner(f"Translating to {selected_lang}..."):
                translated = translate_text(
                    st.session_state["simplified"], lang_code
                )
            st.session_state["translated"] = translated
            st.session_state["lang_code"] = lang_code

        if "translated" in st.session_state:
            st.text_area("Translated Text", st.session_state["translated"], height=200)

            # --- Step 5: Audio ---
            st.subheader("🔊 Step 5: Listen")
            if st.button("🔈 Generate Audio"):
                with st.spinner("Generating audio..."):
                    audio_path = generate_audio(
                        st.session_state["translated"],
                        st.session_state["lang_code"],
                    )
                st.audio(audio_path, format="audio/mp3")
                st.success(f"Audio saved to: {audio_path}")

    # Cleanup temp file
    os.unlink(temp_path)
