from pprint import pprint

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.jd_skill_extractor import extract_jd_skills
from services.jd_matcher import match_job_description
from services.role_analysis_service import analyze_role_fit


PDF_PATH = "../uploads/Resume.pdf"


job_description = """
Software Engineer

We are looking for a Software Engineer to build scalable web applications.

Requirements:
- Strong experience with Python and FastAPI
- Experience building frontend applications using React
- Knowledge of SQL and MySQL
- Experience with Docker and AWS
- Understanding of REST APIs
- Familiarity with Git and GitHub
- Knowledge of Machine Learning is a plus

The candidate should have strong problem-solving and communication skills.
"""


# ------------------------------------------------------------
# Extract resume
# ------------------------------------------------------------

text = extract_text_from_pdf(PDF_PATH)

resume = extract_resume(text)


# ------------------------------------------------------------
# Extract JD skills
# ------------------------------------------------------------

jd_skills = extract_jd_skills(
    job_description
)


# ------------------------------------------------------------
# Match resume against JD
# ------------------------------------------------------------

resume_skills = resume.get(
    "skills",
    []
)

match_result = match_job_description(
    resume_skills,
    jd_skills
)


# ------------------------------------------------------------
# Generate role-specific analysis
# ------------------------------------------------------------

role_analysis = analyze_role_fit(
    resume_info=resume,
    job_description=job_description,
    matched_skills=match_result["matched_skills"],
    missing_skills=match_result["missing_skills"],
)


# ------------------------------------------------------------
# Print results
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("ROLE-SPECIFIC RESUME ANALYSIS")
print("=" * 60)

print("\nJob Match:")
print(
    match_result["match_percentage"],
    "%"
)

print("\nRole Fit Summary:")
print(
    role_analysis["role_fit_summary"]
)

print("\nStrong Matches:")

for item in role_analysis["strong_matches"]:
    print("•", item)

print("\nWeak / Underrepresented:")

for item in role_analysis["weak_or_underrepresented"]:
    print("•", item)

print("\nMissing Requirements:")

for item in role_analysis["missing_requirements"]:
    print("•", item)

print("\nResume Improvements:")

for item in role_analysis["resume_improvements"]:
    print("•", item)

print("\nKeyword Recommendations:")

for item in role_analysis["keyword_recommendations"]:
    print("•", item)

print("\nPriority Actions:")

for item in role_analysis["priority_actions"]:
    print("•", item)