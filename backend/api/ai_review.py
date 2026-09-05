from fastapi import APIRouter, UploadFile, File
import os

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.ai_resume_review import review_resume
from utils.logger import logger

router = APIRouter()

UPLOAD_FOLDER = "../uploads"


@router.post("/ai-review")
async def ai_review(file: UploadFile = File(...)):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    logger.info(f"AI Review: Resume uploaded ({file.filename})")

    text = extract_text_from_pdf(file_path)

    resume_info = extract_resume(text)

    logger.info("AI Review: Resume extracted successfully.")

    review = review_resume(resume_info, text)

    logger.info("AI Review generated successfully.")

    return {
        "resume_info": resume_info,
        "ai_review": review
    }