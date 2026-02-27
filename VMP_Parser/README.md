# 💊 Vernacular Medical Prescription Parser (VMP_Parser)

A smart tool that reads medical prescriptions (handwritten or printed), extracts medicine details using OCR, simplifies them using AI, translates into regional languages, and provides audio playback.

## 🚀 Features

- **OCR Extraction** — Reads prescription images using Tesseract OCR
- **Smart Parsing** — Expands medical abbreviations and extracts dosage, frequency, duration
- **AI Simplification** — Uses Google Gemini to explain prescriptions in simple language
- **Translation** — Supports English, Telugu, and Hindi
- **Text-to-Speech** — Generates audio output using gTTS

## 📁 Folder Structure

```
VMP_Parser/
├── backend/
│   ├── app.py                # Streamlit main application
│   ├── config.py             # Configuration and environment variables
│   ├── modules/
│   │   ├── ocr.py            # Image preprocessing & text extraction
│   │   ├── parser.py         # Abbreviation expansion & data extraction
│   │   ├── llm.py            # LLM-based prescription simplification
│   │   ├── translator.py     # Multi-language translation
│   │   ├── tts.py            # Text-to-speech audio generation
│   │   └── utils.py          # Utility helper functions
│   ├── data/
│   │   ├── abbreviation_map.json
│   │   └── sample_prescriptions/
│   ├── output/               # Generated audio files
│   └── requirements.txt
├── README.md
└── .env                      # API keys (not committed)
```

## 🛠️ Installation

### Prerequisites
- Python 3.9+
- Tesseract OCR installed on your system
  - **Ubuntu/Debian:** `sudo apt install tesseract-ocr`
  - **macOS:** `brew install tesseract`
  - **Windows:** Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

### Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd VMP_Parser

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment variables
# Edit .env and add your Gemini API key
```

## ▶️ How to Run

```bash
cd VMP_Parser
streamlit run backend/app.py
```

The app will open in your browser at `http://localhost:8501`.

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Your Google Gemini API key |

## 🔮 Future Improvements

- Support for more languages (Tamil, Kannada, Malayalam, Bengali)
- Handwriting recognition fine-tuning with custom models
- Drug interaction warnings
- Prescription history tracking with database storage
- Mobile-friendly PWA version
- PDF prescription support
- Doctor-patient messaging integration
