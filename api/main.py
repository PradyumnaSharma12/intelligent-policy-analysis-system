from fastapi import FastAPI, UploadFile, File
from app.utils.pdf_reader import extract_text_from_pdf
from app.utils.gemini_service import generate_policy_summary
from app.utils.vector_store import create_vector_store, save_vector_store
from app.utils.rag_service import ask_policy
from pydantic import BaseModel
from app.utils.classifier_service import classify_text
from app.utils.recommendation_service import get_recommendations
import shutil
import os

app = FastAPI(title="Intelligent AI-Based Policy Analysis and Recommendation System")


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
    recommended_policies = get_recommendations(predicted_category)

    vector_store = create_vector_store(extracted_text)

    save_vector_store(vector_store)

    return {
        "filename": file.filename,
        "characters_extracted": len(extracted_text),
        "predicted_category": predicted_category,
        "recommended_policies": recommended_policies,
        "message": "Policy uploaded and indexed successfully",
    }


@app.post("/summarize-policy")
async def summarize_policy(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    summary = generate_policy_summary(extracted_text)

    return {"filename": file.filename, "summary": summary}


@app.post("/ask-policy")
async def ask_policy_endpoint(request: QuestionRequest):

    answer = ask_policy(request.question)

    return {"question": request.question, "answer": answer}
