from services.jd_matcher import match_job_description


resume_skills = [
    "Python",
    "React.js",
    "FastAPI",
    "MySQL",
    "Git",
    "GitHub",
    "Machine Learning",
    "Pandas",
]


jd_skills = [
    "Python",
    "React",
    "FastAPI",
    "Docker",
    "AWS",
    "SQL",
]


result = match_job_description(
    resume_skills,
    jd_skills
)


print("\n" + "=" * 60)
print("JOB MATCH RESULT")
print("=" * 60)

print("Match Percentage:", result["match_percentage"])

print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print("•", skill)

print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print("•", skill)

print("\nAdditional Resume Skills:")
for skill in result["additional_resume_skills"]:
    print("•", skill)

print("\nStatistics:")
print("Total JD Skills:", result["total_jd_skills"])
print("Matched:", result["matched_count"])
print("Missing:", result["missing_count"])