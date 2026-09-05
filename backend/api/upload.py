from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.resume_validator import is_valid_resume
from utils.logger import logger

router = APIRouter()

UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"Resume uploaded successfully: {file.filename}")

    text = ""

    if file.filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
        if not is_valid_resume(text):
            os.remove(file_path)
            logger.warning(f"Invalid resume document rejected: {file.filename}")

            raise HTTPException(
                status_code=400,
                detail="Please upload a valid resume document."
            )

    resume_info = extract_resume(text)

    logger.info("Resume information extracted successfully.")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "resume_info": resume_info,
        "resume_text": text
    }