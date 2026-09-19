import json
import logging
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError, ServerError

load_dotenv()

logger = logging.getLogger(__name__)

MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 1


def improve_resume(resume_data: dict) -> dict:
    """
    Generate truthful, ATS-friendly improvements for an existing resume.

    The AI must improve wording and presentation without inventing
    experience, skills, metrics, projects, or achievements.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured."
        )

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.5-flash"
    )

    client = genai.Client(api_key=api_key)

    resume_json = json.dumps(
        resume_data,
        ensure_ascii=False,
        indent=2
    )

    prompt = f"""
You are a professional resume writer, ATS optimization specialist,
and technical recruiter.

Improve the candidate's EXISTING resume.

CURRENT DATE: 2026-08-30

IMPORTANT RULES:

1. Use ONLY information contained in the supplied resume.

2. Never invent skills, technologies, projects, jobs, certifications,
   achievements, responsibilities, metrics, employers, or education.

3. Never fabricate numerical results.

4. Never add a technology simply because it is popular or desirable.

5. Preserve the candidate's actual meaning and experience.

6. Improve wording, clarity, readability, structure, and ATS compatibility.

7. Prefer strong action verbs over passive wording.

8. Make bullets concise and achievement-oriented only where the supplied
   information supports the achievement. Never create or strengthen an
   achievement that is not explicitly supported.

9. Preserve genuine metrics already present in the resume.

10. If a bullet lacks a measurable result, do NOT invent one.

11. If an improvement would require information not present in the resume,
    clearly mark it as conditional.

12. Remove genuinely redundant skills and terminology where appropriate.

13. Keep distinct technologies separate when they represent different
    competencies. For example, SQL and MySQL are related but should not
    automatically be treated as duplicates.

14. Do not keyword-stuff the resume.

15. Do not change education dates or employment dates.

16. Use the CURRENT DATE when describing education status.

17. If a degree started in the past and its end date is in the future,
    describe it as currently pursuing/in progress.

18. Do not rewrite the candidate's resume into a completely different
    profile. Preserve the candidate's actual technical direction.

19. Do not introduce new technical concepts, methodologies, architectures,
    security mechanisms, design patterns, performance claims, or industry
    terminology as factual claims unless the ORIGINAL BULLET itself provides
    evidence for them.

20. Do not infer implementation details from a project's technology list.
    A technology listed for a project may be mentioned in the improved bullet
    only when doing so does not introduce a new factual claim.

21. Do not strengthen a claim merely to make it sound more impressive.
    Preserve the factual meaning, scope, and certainty of the original bullet.

22. Do not convert vague evidence into a specific implementation claim.
    For example, "SQL database" must not automatically become "MySQL database
    schema" unless the original bullet explicitly establishes that connection.

23. Do not add performance, scalability, security, availability, architecture,
    optimization, deployment, or implementation claims unless those claims
    are already supported by the original bullet or explicit resume evidence.

24. Every "improved" version must remain factually equivalent to its
    corresponding "original" version.

25. If a potentially useful technical detail exists elsewhere in the resume
    but is not established in the original bullet, do not insert it into the
    rewritten bullet. Instead, mention it as a conditional recommendation in
    "important_notes".

26. Never fabricate or upgrade metrics. Existing metrics may be preserved,
    but new metrics, percentages, performance claims, scale claims, or
    outcomes must not be created.

27. Do not optimize ATS keywords by moving technologies from a project's
    technology list into its description.

28. Do not recommend adding an acronym or alternate terminology solely to
    increase keyword coverage when the original resume already contains the
    corresponding concept.

29. ATS improvements must focus on truthful improvements to wording,
    formatting, section organization, terminology consistency, and
    explicit concepts already supported by the resume.

30. Never claim that an ATS improvement was made merely because a keyword
    was moved from project metadata into a bullet.

FOCUS AREAS:

- Professional summary
- Education clarity
- Experience bullet quality
- Project bullet quality
- Skills organization
- Duplicate terminology
- Readability
- ATS-friendly wording
- Technical specificity
- Quantifiable achievements already supported by the resume

For every rewritten bullet, provide the original and improved versions.

Return ONLY valid JSON using exactly this structure:

{{
    "professional_summary": {{
        "original": "Existing summary if present, otherwise empty string.",
        "improved": "Improved summary based only on the resume evidence."
    }},

    "education_improvements": [
        {{
            "original": "Original education entry or relevant text.",
            "improved": "Improved version.",
            "reason": "Why the change improves clarity."
        }}
    ],

    "experience_improvements": [
        {{
            "section": "Experience section name",
            "original": "Original bullet.",
            "improved": "Improved bullet.",
            "reason": "Why the wording is stronger."
        }}
    ],

    "project_improvements": [
        {{
            "project": "Project name",
            "original": "Original bullet.",
            "improved": "Improved bullet.",
            "reason": "Why the wording is stronger."
        }}
    ],

    "skills_improvements": {{
        "duplicates_to_remove": [],
        "recommended_structure": {{
            "Languages": [],
            "Frameworks & Libraries": [],
            "Databases": [],
            "Developer Tools": [],
            "Other": []
        }},
        "notes": []
    }},

    "readability_improvements": [
        "Concrete readability improvement."
    ],

    "ats_improvements": [
        "Concrete ATS improvement supported by the resume."
    ],

    "important_notes": [
        "Important conditional recommendation or missing information."
    ]
}}

RESUME DATA:

{resume_json}
"""

    try:
        logger.info(
            "Sending resume to Gemini for improvement."
        )

        response = None

        # Retry temporary Gemini 503 errors.
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                break

            except ServerError as error:
                if attempt >= MAX_RETRIES:
                    logger.error(
                        "Gemini remained unavailable after %s attempts.",
                        MAX_RETRIES
                    )

                    raise RuntimeError(
                        "The AI service is temporarily unavailable. "
                        "Please try again in a few moments."
                    ) from error

                delay = INITIAL_RETRY_DELAY * (2 ** (attempt - 1))

                logger.warning(
                    "Gemini returned 503 UNAVAILABLE. "
                    "Retrying in %s seconds (attempt %s/%s).",
                    delay,
                    attempt,
                    MAX_RETRIES
                )

                time.sleep(delay)

        if response is None:
            raise RuntimeError(
                "The AI service did not return a response."
            )

        text = response.text.strip()

        # Remove markdown code fences if Gemini returns them.
        if text.startswith("```json"):
            text = text[7:]

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        result = json.loads(text)

        logger.info(
            "Resume improvement generated successfully."
        )

        return result

    except ClientError as error:

        status_code = getattr(error, "status_code", None)

        # Gemini quota / rate limit
        if status_code == 429 or "RESOURCE_EXHAUSTED" in str(error):
            logger.warning(
                "Gemini API quota exceeded while improving resume."
            )

            raise RuntimeError(
                "The AI service quota has been reached. "
                "Please wait and try again later."
            ) from error

        # Invalid API key / authentication
        if status_code in (401, 403):
            logger.error(
                "Gemini API authentication failed."
            )

            raise RuntimeError(
                "The AI service authentication failed. "
                "Please check the Gemini API configuration."
            ) from error

        logger.exception(
            "Gemini API error while improving resume."
        )

        raise RuntimeError(
            "The AI service could not generate resume improvements. "
            "Please try again later."
        ) from error

    except json.JSONDecodeError as error:

        logger.exception(
            "Gemini returned invalid JSON for resume improvement."
        )

        raise RuntimeError(
            "The AI returned an invalid response. "
            "Please try again."
        ) from error

    except Exception as error:

        logger.exception(
            "Unexpected error while generating resume improvements."
        )

        raise RuntimeError(
            "Unable to generate resume improvements. "
            "Please try again later."
        ) from error
