from fastapi import FastAPI, UploadFile, File
from app.utils.pdf_reader import extract_text_from_pdf
from app.utils.gemini_service import generate_policy_summary
import shutil
import os

app = FastAPI(title="Intelligent AI-Based Policy Analysis and Recommendation System")

UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"status": "success", "message": "Policy AI FastAPI Backend Running"}


@app.post("/upload-policy")
async def upload_policy(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "characters_extracted": len(extracted_text),
        "preview": extracted_text[:1000],
    }


@app.post("/summarize-policy")
async def summarize_policy(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    summary = generate_policy_summary(extracted_text)

    return {"filename": file.filename, "summary": summary}
