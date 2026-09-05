from fastapi import APIRouter

from schemas.resume_schema import ResumeInfo
from services.ats_service import calculate_ats_score
from utils.logger import logger

router = APIRouter()


@router.post("/calculate-ats")
def calculate_ats(resume: ResumeInfo):
    score = calculate_ats_score(resume.model_dump())
    logger.info("ATS score calculated successfully.")

    return {
        "resume_info": resume.model_dump(),
        "ats_result": score
    }