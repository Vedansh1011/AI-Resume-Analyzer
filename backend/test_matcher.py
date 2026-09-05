from services.jd_matcher import match_job_description

resume_skills = [
    "Python",
    "FastAPI",
    "React",
    "Git",
    "SQL"
]

jd_skills = [
    "Python",
    "FastAPI",
    "Docker",
    "AWS",
    "Git"
]

result = match_job_description(
    resume_skills,
    jd_skills
)

print(result)