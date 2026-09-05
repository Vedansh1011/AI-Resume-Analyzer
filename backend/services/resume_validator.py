import re


RESUME_SECTIONS = [
    "education",
    "experience",
    "work experience",
    "professional experience",
    "employment",
    "skills",
    "technical skills",
    "projects",
    "academic projects",
    "certifications",
    "achievements",
    "objective",
    "summary",
    "profile",
]


def is_valid_resume(text: str) -> bool:
    """
    Check whether extracted PDF text appears to be a resume.

    The validation is intentionally flexible because resumes can
    have different structures, especially for freshers.
    """

    if not text or len(text.strip()) < 100:
        return False

    normalized_text = re.sub(r"\s+", " ", text.lower())

    # Count resume-specific section indicators.
    section_matches = sum(
        1
        for section in RESUME_SECTIONS
        if re.search(rf"\b{re.escape(section)}\b", normalized_text)
    )

    # Basic contact information indicators.
    has_email = bool(
        re.search(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            text
        )
    )

    has_phone = bool(
        re.search(
            r"(?<!\d)(?:\+?\d[\d\s().-]{8,}\d)(?!\d)",
            text
        )
    )

    # A resume should normally contain multiple resume-specific signals.
    score = section_matches

    if has_email:
        score += 1

    if has_phone:
        score += 1

    return score >= 3