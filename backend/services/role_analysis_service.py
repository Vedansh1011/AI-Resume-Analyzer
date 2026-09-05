import json
import logging
import os

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


def analyze_role_fit(
    resume_info: dict,
    job_description: str,
    matched_skills: list[str],
    missing_skills: list[str],
) -> dict:
    """
    Generate role-specific resume recommendations.

    The analysis focuses on how the existing resume can be improved
    for the supplied job description. It must not invent experience
    or recommend falsely adding skills.
    """

    resume_json = json.dumps(
        resume_info,
        ensure_ascii=False
    )

    matched_json = json.dumps(
        matched_skills,
        ensure_ascii=False
    )

    missing_json = json.dumps(
        missing_skills,
        ensure_ascii=False
    )

    prompt = f"""
        You are a professional technical recruiter, ATS consultant, and resume reviewer.

        CURRENT DATE: 2026-08-29

        Use this current date when interpreting all resume timelines, especially
        education and employment dates.

        Analyze how well the candidate's EXISTING resume fits the supplied job description.

        IMPORTANT TRUTHFULNESS AND EVIDENCE RULES:

        1. Use only information actually present in the supplied resume data.
        2. Never invent skills, technologies, experience, projects, certifications,
        achievements, responsibilities, or outcomes.
        3. Never recommend adding a skill merely because it appears in the job
        description.
        4. A missing skill must remain classified as missing unless the resume
        provides evidence that the candidate already has that skill.
        5. If a technology is strongly implied by an existing technology but is not
        explicitly demonstrated, classify it as "weak_or_underrepresented",
        NOT as an existing skill.
        6. If a missing skill could reasonably be demonstrated through an existing
        project or experience, explain how to make that existing experience
        clearer. Do not tell the candidate to falsely claim the skill.
        7. If a missing skill is genuinely absent from the resume, clearly say that
        it should NOT be added unless the candidate actually has the experience.
        8. Never recommend keyword stuffing.

        SKILL EVIDENCE RULES:

        9. Distinguish between:
        - directly demonstrated skills
        - skills listed but weakly demonstrated
        - related/implied skills
        - genuinely missing skills
        10. A skill appearing only in the Skills section is weaker evidence than a
            skill demonstrated in a project or experience description.
        11. Do not treat related technologies as duplicates when they represent
            different competencies. For example:
            - Git and GitHub are related but distinct.
            - SQL and MySQL are related but distinct.
        12. Identify true duplicate variants such as:
            - React / React.js / ReactJS
            - Node / Node.js / NodeJS
            - Scikit-Learn / Scikit Learn
            Only recommend consolidation when the terms are genuinely redundant.

        KEYWORD RECOMMENDATION RULES:

        13. Only recommend a keyword for explicit inclusion when the resume already
            provides evidence for that technology or concept.
        14. When the resume supports the concept but does not use the exact JD wording,
            recommend making the existing experience more explicit.
        15. Example of GOOD advice:
            "If the FastAPI project uses REST endpoints, explicitly describe those
            endpoints in the project bullet before adding 'REST APIs' as a keyword."
        16. Example of BAD advice:
            "Add REST APIs to your Skills section because the JD requires it."
        17. For genuinely missing skills such as AWS or Docker, state that they are
            missing and recommend gaining relevant experience first. Do not suggest
            falsely adding them to the resume.

        RESUME QUALITY RULES:

        18. Review readability and scanability.
        19. Identify duplicate words, repeated technologies, redundant phrases, and
            inconsistent terminology where they materially affect resume quality.
        20. Review bullet points for:
            - weak/passive verbs
            - vague statements
            - missing technical contribution
            - missing measurable outcomes
            - excessive repetition
        21. Recommend concrete improvements to existing bullets rather than generic
            advice.
        22. Consider project relevance to the target role.
        23. Consider experience relevance to the target role.
        24. Prioritize the changes that would have the greatest impact on the
            candidate's application.
        25. Do not rewrite the entire resume.
        26. Never provide a resume bullet as a factual statement unless the supplied
            resume data explicitly supports that activity. When suggesting a possible
            rewrite based on an inferred or unverified activity, clearly label it as
            conditional using wording such as "If you actually did this..." or
            "If this accurately reflects your project...".
        27. If a skill is listed in the resume but has no supporting evidence elsewhere,
            do not assume that the candidate used it. Recommend either:
            - adding truthful evidence if the candidate actually used it, or
            - removing the skill until genuine experience is obtained.
        28. Never convert an inferred skill into a confirmed skill merely because two
            technologies commonly appear together.
        29. Do not describe an education entry as "future-dated" merely because its
            end date is later than the current date. Determine whether the candidate
            is currently pursuing, upcoming, or has completed the program based on
            the education dates and the current date.
        30. Do not assume that a skill listed in the Skills section was actually used
            in a project or job. Skills-only evidence should remain skills-only
            evidence.
        31. If Git, GitHub, Docker, AWS, REST APIs, or any other technology is listed
            without supporting project or experience evidence, do not instruct the
            candidate to claim that technology was used.
        32. When recommending that an unsupported skill be demonstrated in a project,
            always use conditional wording:
            "If you actually used X, document how you used it."
            Never present an unverified activity as a resume fact.
        33. Keyword recommendations must distinguish between:
            - an exact keyword that is already supported by resume evidence,
            - an existing concept that should be described more explicitly,
            - a genuinely missing skill that should not be added yet.
        34. Never recommend adding a genuinely missing technology to the resume just
            to improve ATS matching. Recommend gaining genuine experience first.
        35. For education timelines, compare the listed dates against the CURRENT DATE
            provided above.

            - If the start date is in the future, describe the program as upcoming,
            incoming, admitted, or expected to start.
            - If the start date has already passed and the end date is in the future,
            describe the program as currently pursuing/in progress.
            - If the end date has already passed, describe it as completed unless the
            resume explicitly indicates otherwise.
            - Never call a program "upcoming" when its stated start date has already
            passed.
            - Never assume a degree is currently being pursued without considering
            both its dates and any status information in the resume.
        36. "missing_requirements" must contain only actual technical skills,
            technologies, tools, qualifications, or other explicit requirements
            from the job description that are not sufficiently supported by the
            resume.
        37. Do not put general resume weaknesses such as lack of professional
            experience, weak bullet points, readability problems, or limited
            industry exposure inside "missing_requirements". Put those in
            "weak_or_underrepresented" or "resume_improvements" instead.
        38. If a requirement is not a skill or qualification but is an experience
            expectation from the job description, describe it accurately rather
            than presenting it as a missing technical skill.
        39. If a requirement is strongly implied or partially supported by existing
            resume evidence but is not explicitly stated, classify it as
            "weak_or_underrepresented" rather than "missing_requirements".

        40. Do not place the same requirement in both "weak_or_underrepresented" and
            "missing_requirements". Each requirement must appear in only one category.

        41. Use "missing_requirements" only when there is insufficient evidence that
            the candidate has the skill, technology, or qualification at all.

        Return ONLY valid JSON using exactly this structure:

        {{
            "role_fit_summary": "Short assessment of the candidate's fit for this role.",

            "strong_matches": [
                "Explain which requirements are directly demonstrated and where."
            ],

            "weak_or_underrepresented": [
                "Explain requirements that may be relevant but are not clearly demonstrated."
            ],

            "missing_requirements": [
                "List genuinely missing requirements from the JD."
            ],

            "resume_improvements": [
                "Give concrete, truthful improvements to the existing resume."
            ],

            "keyword_recommendations": [
                "A job-description keyword may only be recommended for explicit inclusion
                when the resume already contains credible evidence of that skill or concept.
                If evidence is absent, classify it as missing rather than recommending it
                as a resume keyword."
            ],

            "priority_actions": [
                "List the highest-value actions in priority order."
            ]
        }}

        RESUME DATA:

        {resume_json}

        MATCHED JOB SKILLS:

        {matched_json}

        MISSING JOB SKILLS:

        {missing_json}

        JOB DESCRIPTION:

        {job_description}
        """

    try:
        logger.info(
            "Generating role-specific resume analysis."
        )

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

        return {
            "role_fit_summary": result.get(
                "role_fit_summary",
                ""
            ),
            "strong_matches": result.get(
                "strong_matches",
                []
            ),
            "weak_or_underrepresented": result.get(
                "weak_or_underrepresented",
                []
            ),
            "missing_requirements": result.get(
                "missing_requirements",
                []
            ),
            "resume_improvements": result.get(
                "resume_improvements",
                []
            ),
            "keyword_recommendations": result.get(
                "keyword_recommendations",
                []
            ),
            "priority_actions": result.get(
                "priority_actions",
                []
            ),
        }

    except Exception:
        logger.exception(
            "Role-specific resume analysis failed."
        )

        return {
            "role_fit_summary": "",
            "strong_matches": [],
            "weak_or_underrepresented": [],
            "missing_requirements": [],
            "resume_improvements": [],
            "keyword_recommendations": [],
            "priority_actions": [],
        }