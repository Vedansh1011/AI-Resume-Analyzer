from fastapi import APIRouter, UploadFile, File, HTTPException

import os

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.resume_validator import is_valid_resume
from services.ats_service import calculate_ats_score
from services.ai_resume_review import review_resume
from utils.logger import logger

router = APIRouter()

UPLOAD_FOLDER = "../uploads"


@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    # Check file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF resume."
        )

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    logger.info(f"Resume uploaded: {file.filename}")

    # Extract text from PDF
    text = extract_text_from_pdf(file_path)

    # Validate whether the uploaded PDF is actually a resume
    if not is_valid_resume(text):
        os.remove(file_path)

        logger.warning(
            f"Invalid resume document rejected: {file.filename}"
        )

        raise HTTPException(
            status_code=400,
            detail="Please upload a valid resume document."
        )

    # Extract resume information
    resume_info = extract_resume(text)

    logger.info("Resume extracted successfully.")

    # Calculate ATS score
    ats_result = calculate_ats_score(resume_info, text)

    logger.info("ATS score calculated.")

    # Generate AI review
    ai_review = review_resume(resume_info)

    logger.info("AI review completed.")

    return {
        "resume_info": resume_info,
        "ats_result": ats_result,
        "ai_review": ai_review
    }