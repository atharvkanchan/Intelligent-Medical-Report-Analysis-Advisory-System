from fastapi import FastAPI, UploadFile
from model import summarize_text, answer_question
from utils import extract_pdf, detect_risks

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile):
    text = extract_pdf(file.file)
    summary = summarize_text(text)
    risks = detect_risks(text)
    return {
        "summary": summary,
        "risks": risks,
        "text": text[:1000]
    }

@app.post("/ask")
async def ask(question: str, context: str):
    answer = answer_question(question, context)
    return answer
