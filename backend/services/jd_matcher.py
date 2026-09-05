import re


# Known aliases / equivalent naming variations.
# These are normalization rules, not broad "similarity" rules.
SKILL_ALIASES = {
    "react": "react",
    "react.js": "react",
    "reactjs": "react",

    "node": "node.js",
    "node.js": "node.js",
    "nodejs": "node.js",

    "express": "express.js",
    "express.js": "express.js",
    "expressjs": "express.js",

    "scikit learn": "scikit-learn",
    "scikit-learn": "scikit-learn",
    "sklearn": "scikit-learn",

    "postgres": "postgresql",
    "postgresql": "postgresql",

    "mongo": "mongodb",
    "mongodb": "mongodb",

    "tailwind": "tailwind css",
    "tailwind css": "tailwind css",
}


def normalize_skill(skill: str) -> str:
    """
    Normalize a skill name while preserving meaningful distinctions.
    """

    skill = skill.strip().lower()

    # Normalize whitespace
    skill = re.sub(r"\s+", " ", skill)

    # Normalize common punctuation variations
    skill = skill.replace(" . ", ".")
    skill = skill.replace(" js", ".js") if skill.endswith(" js") else skill

    return SKILL_ALIASES.get(skill, skill)


def normalize_skills(skills: list) -> set:
    """
    Convert skills into a normalized set.
    """

    normalized = set()

    for skill in skills:
        if not isinstance(skill, str):
            continue

        skill = normalize_skill(skill)

        if skill:
            normalized.add(skill)

    return normalized


def match_job_description(
    resume_skills: list,
    jd_skills: list
):
    """
    Compare resume skills with job description skills.

    Returns:
        - match percentage
        - matched skills
        - missing skills
        - resume-only skills
        - total JD skills
    """

    resume_set = normalize_skills(resume_skills)
    jd_set = normalize_skills(jd_skills)

    matched = resume_set.intersection(jd_set)
    missing = jd_set.difference(resume_set)
    resume_only = resume_set.difference(jd_set)

    if jd_set:
        match_percentage = round(
            (len(matched) / len(jd_set)) * 100,
            2
        )
    else:
        match_percentage = 0

    return {
        "match_percentage": match_percentage,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "additional_resume_skills": sorted(resume_only),
        "total_jd_skills": len(jd_set),
        "matched_count": len(matched),
        "missing_count": len(missing),
    }