import logging
import os
import json
import re

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


def review_resume(resume_info: dict, resume_text: str = ""):

    prompt = f"""
You are a professional technical recruiter, ATS specialist,
and resume editor.

Analyze the resume carefully.

Your analysis must be specific to the supplied resume.
Do not give generic advice when you can identify a concrete issue.

Pay particular attention to:

1. Resume strengths
2. Resume weaknesses
3. Duplicate or overlapping skills
4. Duplicate words or unnecessarily repeated terminology
5. Inconsistent technology naming
6. Readability
7. Section organization
8. Bullet-point quality
9. Action verbs
10. Quantifiable achievements
11. Education timeline clarity
12. Professional experience relevance
13. Project quality
14. Missing information that would materially improve the resume
15. Concrete ways to improve the resume

IMPORTANT KEYWORD RULES:

- Never list a skill as a missing keyword if that skill already appears
  anywhere in the supplied resume information or raw resume text.
- "Pandas" and "NumPy", for example, must not be reported as missing
  if they already appear in the resume.
- Do not infer that a concept is missing merely because a particular
  phrase is not used.
- Distinguish between:
    a) missing skills,
    b) alternative terminology,
    c) potentially useful keywords.
- Only identify a keyword as genuinely missing when there is strong
  evidence that the resume lacks that skill or concept.
- Do not recommend adding keywords simply for ATS manipulation.

IMPORTANT:

- Do NOT recommend adding keywords merely to manipulate ATS systems.
- Only recommend keywords or skills that are genuinely relevant.
- Do NOT treat related technologies as duplicates unless they are
  actually redundant.
- For example, Git and GitHub are related but are not identical skills.
- SQL and MySQL are related but are not identical skills.
- React and React.js can reasonably be normalized as the same technology.
- Distinguish between a missing keyword and a missing skill.
- Do not invent experience, technologies, achievements, or metrics.
- Do not claim the candidate has experience that is not present.
- If something cannot be determined from the resume, explicitly say so.

For readability, check for:

- overly long bullets
- passive wording
- generic wording
- repetitive sentence structures
- inconsistent formatting
- dense skill lists
- unclear hierarchy
- unnecessary words
- unclear dates

For improvements, provide practical instructions.

Where useful, provide a BEFORE and AFTER example using only
information already present in the resume.

For potential_keywords:

- Only include terms that are NOT already present in the resume.
- Do not include synonyms or direct variants of skills already present.
- Do not include Pandas, NumPy, Python, React, FastAPI, Java, SQL, MySQL,
  Git, GitHub, Machine Learning, Artificial Intelligence, Scikit-Learn,
  Tailwind CSS, Vite, Power BI, Postman, or other skills already present
  in the supplied resume.
- Only suggest a potential keyword if it would genuinely improve the
  resume for the candidate's stated/targeted technical direction.
- Do not recommend a keyword solely because it is popular in software
  engineering.
- If there are no meaningful potential keywords, return an empty array.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "strengths": [
        "..."
    ],

    "weaknesses": [
        "..."
    ],

    "suggestions": [
        "..."
    ],

    "keyword_analysis": {{
        "duplicates": [
            "..."
        ],
        "overlapping_terms": [
            "..."
        ],
        "inconsistent_terms": [
            "..."
        ],
        "potential_keywords": [
            "..."
        ]
    }},

    "readability": {{
        "issues": [
            "..."
        ],
        "improvements": [
            "..."
        ]
    }},

    "bullet_improvements": [
        {{
            "section": "...",
            "issue": "...",
            "before": "...",
            "after": "..."
        }}
    ],

    "overall_review": "..."
}}

RESUME INFORMATION:

{json.dumps(resume_info, indent=2)}

RAW RESUME TEXT:

{resume_text}
"""

    try:

        logger.info(
            "Sending resume to Gemini for AI review."
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        logger.info(
            "Gemini API responded successfully."
        )

        clean_text = response.text.strip()

        # Remove Markdown JSON fences if Gemini returns them.
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]

        elif clean_text.startswith("```"):
            clean_text = clean_text[3:]

        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]

        clean_text = clean_text.strip()

        review = json.loads(clean_text)

        return review

    except Exception:

        logger.exception(
            "Gemini API failed during resume review."
        )

        return {
            "strengths": [],
            "weaknesses": [],
            "suggestions": [
                "AI review is temporarily unavailable. Please try again later."
            ],
            "keyword_analysis": {
                "duplicates": [],
                "overlapping_terms": [],
                "inconsistent_terms": [],
                "potential_keywords": []
            },
            "readability": {
                "issues": [],
                "improvements": []
            },
            "bullet_improvements": [],
            "overall_review": (
                "AI service is currently unavailable."
            )
        }