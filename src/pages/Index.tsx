import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const Index = () => {
  const modules = [
    { name: "ocr.py", desc: "Image preprocessing & Tesseract text extraction" },
    { name: "parser.py", desc: "Abbreviation expansion, dosage/frequency parsing" },
    { name: "llm.py", desc: "Gemini-powered prescription simplification" },
    { name: "translator.py", desc: "Multi-language translation (EN, TE, HI)" },
    { name: "tts.py", desc: "gTTS audio generation" },
    { name: "utils.py", desc: "Helper functions for text cleaning & file ops" },
  ];

  return (
    <div className="min-h-screen bg-background p-8 max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2">💊 VMP_Parser</h1>
        <p className="text-lg text-muted-foreground">
          Vernacular Medical Prescription Parser — all Python backend files have been generated.
        </p>
      </div>

      <Card className="mb-6">
        <CardHeader>
          <CardTitle>🚀 Quick Start</CardTitle>
        </CardHeader>
        <CardContent>
          <pre className="bg-muted p-4 rounded-md text-sm overflow-x-auto">
{`# Install dependencies
pip install -r VMP_Parser/backend/requirements.txt

# Add your Gemini API key to VMP_Parser/.env

# Run the app
cd VMP_Parser
streamlit run backend/app.py`}
          </pre>
        </CardContent>
      </Card>

      <Card className="mb-6">
        <CardHeader>
          <CardTitle>📁 Generated Files</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-3">
            {modules.map((m) => (
              <div key={m.name} className="flex items-start gap-3 p-3 bg-muted rounded-md">
                <code className="font-mono text-sm font-semibold text-primary whitespace-nowrap">{m.name}</code>
                <span className="text-sm text-muted-foreground">{m.desc}</span>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      <p className="text-sm text-muted-foreground text-center">
        Download the VMP_Parser folder and run locally with Python 3.9+ and Tesseract OCR.
      </p>
    </div>
  );
};

export default Index;
