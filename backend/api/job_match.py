from fastapi import APIRouter, HTTPException
from schemas.job_description_schema import JobDescription
from services.jd_skill_extractor import extract_jd_skills
from services.jd_matcher import match_job_description
from services.role_analysis_service import analyze_role_fit

router = APIRouter()

@router.post("/match-job-description")
def match_job(data: JobDescription):

    # ------------------------------------------------------------
    # 0. Validate input before calling Gemini or other services
    # ------------------------------------------------------------

    if not data.job_description or not data.job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    if not data.resume_skills:
        raise HTTPException(
            status_code=400,
            detail="Resume skills are missing. Please analyze your resume first."
        )

    if not data.resume_data:
        raise HTTPException(
            status_code=400,
            detail="Resume data is missing. Please analyze your resume first."
        )

    # ------------------------------------------------------------
    # 1. Extract technical skills from the full job description
    # ------------------------------------------------------------

    jd_skills = extract_jd_skills(
        data.job_description
    )

    # ------------------------------------------------------------
    # 2. Match resume skills against JD skills
    # ------------------------------------------------------------

    match_result = match_job_description(
        data.resume_skills,
        jd_skills
    )

    # ------------------------------------------------------------
    # 3. Generate role-specific resume analysis
    # ------------------------------------------------------------

    role_analysis = analyze_role_fit(
        resume_info=data.resume_data,
        job_description=data.job_description,
        matched_skills=match_result["matched_skills"],
        missing_skills=match_result["missing_skills"],
    )

    # ------------------------------------------------------------
    # 4. Return complete result
    # ------------------------------------------------------------

    return {
        "job_description_skills": jd_skills,
        "job_match_result": match_result,
        "role_analysis": role_analysis,
    }