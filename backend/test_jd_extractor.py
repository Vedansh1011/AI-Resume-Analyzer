from services.jd_skill_extractor import extract_jd_skills


job_description = """
We are looking for a Software Engineer to build scalable web applications.

Requirements:

- Strong experience with Python and FastAPI
- Experience building frontend applications using React
- Knowledge of SQL and MySQL
- Experience with Docker and AWS
- Understanding of REST APIs
- Familiarity with Git and GitHub
- Knowledge of Machine Learning is a plus

Good communication and problem-solving skills are required.
"""


skills = extract_jd_skills(job_description)


print("\n" + "=" * 60)
print("JOB DESCRIPTION SKILLS")
print("=" * 60)

for skill in skills:
    print("•", skill)

print("\nTotal Skills:", len(skills))