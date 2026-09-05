import re
from utils.text_cleaner import clean_lines

# Skills database (we'll expand this later)
SKILLS_DB = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "MySQL",
    "FastAPI",
    "React",
    "React.js",
    "Tailwind CSS",
    "Machine Learning",
    "Artificial Intelligence",
    "Scikit-Learn",
    "Pandas",
    "NumPy",
    "Git",
    "GitHub",
    "Power BI",
    "Postman",
    "Vite",
    "Axios",
    "Jupyter Notebook"
]

def extract_name(text: str):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines[0] if lines else ""

def extract_email(text: str):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group() if match else ""

def extract_phone(text: str):

    match = re.search(
        r"\+?\d[\d\s\-]{8,}\d",
        text
    )

    return match.group().strip() if match else ""

def extract_skills(text: str):

    found = []

    lower_text = text.lower()

    for skill in SKILLS_DB:
        if skill.lower() in lower_text:
            found.append(skill)

    return sorted(found)

def extract_education(text: str):

    education = []

    # Extract only the Education section
    pattern = r"Education(.*?)Relevant Coursework"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if not match:
        return education

    section = match.group(1)

    lines = [line.strip() for line in section.split("\n") if line.strip()]

    i = 0

    while i < len(lines):

        if (
            i + 3 < len(lines)
            and ("Bachelor" in lines[i + 2] or "Master" in lines[i + 2])
        ):

            education.append({
                "institution": lines[i],
                "duration": lines[i + 1],
                "degree": lines[i + 2],
                "location": lines[i + 3]
            })

            i += 4

        else:
            i += 1

    return education

def extract_experience(text: str):
    """
    Extract work experience from the resume.
    """

    experience = []

    pattern = r"Experience(.*?)Projects"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if not match:
        return experience

    section = match.group(1)

    lines = clean_lines(section.split("\n"))

    i = 0

    while i < len(lines):

        if i + 3 < len(lines):

            company = lines[i]
            duration = lines[i + 1]
            role = lines[i + 2]
            location = lines[i + 3]

            description = []
            j = i + 4

            while j < len(lines) and lines[j].startswith("•"):
                description.append(lines[j].lstrip("• ").strip())
                j += 1

            experience.append({
                "company": company,
                "duration": duration,
                "role": role,
                "location": location,
                "description": description
            })

            i = j

        else:
            break

    return experience

def extract_projects(text: str):

    projects = []

    pattern = r"Projects(.*?)Technical Skills"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if not match:
        return projects

    section = match.group(1)

    lines = clean_lines(section.split("\n"))

    current_project = None

    for line in lines:

        # New project starts
        if "|" in line:

            # Save previous project
            if current_project:
                projects.append(current_project)

            title, tech = line.split("|", 1)

            current_project = {
                "project_name": title.strip(),
                "technologies": [
                    t.strip() for t in tech.split(",")
                ],
                "description": []
            }

        elif line.startswith("•") and current_project:

            current_project["description"].append(
                line.lstrip("• ").strip()
            )

    # Save the final project
    if current_project:
        projects.append(current_project)

    return projects


def extract_resume(text: str):

    return {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "skills": extract_skills(text),

        "education": extract_education(text),

        "experience": extract_experience(text),

        "projects": extract_projects(text)

    }