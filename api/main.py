from fastapi import FastAPI, UploadFile, File
from app.utils.pdf_reader import extract_text_from_pdf
from app.utils.gemini_service import generate_policy_summary
from app.utils.vector_store import create_vector_store, save_vector_store
from app.utils.rag_service import ask_policy
from pydantic import BaseModel
from app.utils.classifier_service import classify_text
from app.utils.gemini_service import generate_policy_recommendations
from app.utils.gemini_service import generate_policy_analysis
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI(title="Intelligent AI-Based Policy Analysis and Recommendation System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


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
    predicted_category = classify_text(extracted_text[:5000])
    try:
        ai_recommendations = generate_policy_recommendations(
            predicted_category, extracted_text
        )
    except Exception:
        ai_recommendations = "Gemini quota exceeded."

    try:
        policy_analysis = generate_policy_analysis(extracted_text)
    except Exception:
        policy_analysis = "Gemini quota exceeded."

    vector_store = create_vector_store(extracted_text)

    save_vector_store(vector_store)

    return {
        "filename": file.filename,
        "characters_extracted": len(extracted_text),
        "predicted_category": predicted_category,
        "ai_recommendations": ai_recommendations,
        "policy_analysis": policy_analysis,
        "message": "Policy uploaded and indexed successfully",
    }


@app.post("/summarize-policy")
async def summarize_policy(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    try:
        summary = generate_policy_summary(extracted_text)
    except Exception:
        summary = "Summary unavailable. Gemini quota exceeded."

    return {"filename": file.filename, "summary": summary}


@app.post("/ask-policy")
async def ask_policy_endpoint(request: QuestionRequest):

    try:
        answer = ask_policy(request.question)
    except Exception:
        answer = "RAG answer unavailable. Gemini quota exceeded."

    return {"question": request.question, "answer": answer}
