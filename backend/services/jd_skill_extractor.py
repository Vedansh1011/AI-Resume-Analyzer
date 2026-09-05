import logging
import os
import json

from dotenv import load_dotenv
from google import genai

logger = logging.getLogger(__name__)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash"
)


def extract_jd_skills(job_description: str) -> list:
    """
    Extract relevant technical skills from a job description.

    Returns a clean list of skills that can be passed to the
    deterministic job matching service.
    """

    prompt = f"""
You are a technical recruiter and job-description analyzer.

Extract the technical skills explicitly required or strongly preferred
in the following job description.

Focus on skills relevant to software engineering, data science,
machine learning, AI, databases, cloud, DevOps, and web development.

Include things such as:

- Programming languages
- Frameworks
- Libraries
- Databases
- Cloud platforms
- Developer tools
- APIs
- Machine learning technologies
- Software engineering concepts when explicitly required

Do NOT extract:

- Company names
- Job titles
- Soft skills such as communication or leadership
- Generic words such as "computer", "technology", or "software"
- Benefits
- Education requirements unless they are a technical certification
- Years of experience

Important:

- Return only skills that are actually present in the job description.
- Do not invent skills.
- Preserve recognizable technology names.
- Avoid duplicate skills.
- Use standard names where possible.
- Return ONLY valid JSON.

Format:

{{
    "skills": [
        "Python",
        "FastAPI",
        "React",
        "Docker"
    ]
}}

JOB DESCRIPTION:

{job_description}
"""

    try:

        logger.info("Extracting skills from job description.")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        clean_text = response.text.strip()

        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]

        elif clean_text.startswith("```"):
            clean_text = clean_text[3:]

        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]

        clean_text = clean_text.strip()

        result = json.loads(clean_text)

        skills = result.get("skills", [])

        if not isinstance(skills, list):
            return []

        # Remove duplicates while preserving order.
        cleaned_skills = []
        seen = set()

        for skill in skills:

            if not isinstance(skill, str):
                continue

            skill = skill.strip()

            if not skill:
                continue

            key = skill.lower()

            if key not in seen:
                seen.add(key)
                cleaned_skills.append(skill)

        logger.info(
            "Extracted %d job description skills.",
            len(cleaned_skills)
        )

        return cleaned_skills

    except Exception as e:

        logger.exception(
            "Failed to extract skills from job description."
        )

        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            raise RuntimeError(
                "Gemini API quota has been exceeded. "
                "Please try again after the quota resets."
            )

        raise RuntimeError(
            "Unable to extract skills from the job description."
        )