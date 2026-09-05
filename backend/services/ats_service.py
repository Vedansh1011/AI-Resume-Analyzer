import re


def _contains_any(text: str, words: list[str]) -> bool:
    return any(
        re.search(
            r"\b" + re.escape(word) + r"\b",
            text,
            re.IGNORECASE
        )
        for word in words
    )


def _count_matches(text: str, words: list[str]) -> int:
    return sum(
        1
        for word in words
        if re.search(
            r"\b" + re.escape(word) + r"\b",
            text,
            re.IGNORECASE
        )
    )


def _normalize_skill(skill: str) -> str:
    """
    Normalize skill names for comparison.
    """
    skill = skill.strip().lower()

    aliases = {
        "react.js": "react",
        "reactjs": "react",
        "node.js": "node",
        "nodejs": "node",
        "scikit learn": "scikit-learn",
        "scikitlearn": "scikit-learn",
        "rest api": "rest apis",
    }

    return aliases.get(skill, skill)


def _collect_text(items: list[dict], key: str) -> list[str]:
    """
    Collect description text from resume sections.
    """
    result = []

    for item in items:
        if not isinstance(item, dict):
            continue

        values = item.get(key, [])

        if isinstance(values, str):
            result.append(values)

        elif isinstance(values, list):
            result.extend(
                value
                for value in values
                if isinstance(value, str)
            )

    return result


def calculate_ats_score(
    resume_info: dict,
    resume_text: str = ""
):
    """
    Calculate a professional ATS-oriented resume score.

    Scoring philosophy:
    - Reward meaningful technical content.
    - Penalize duplicate/overlapping skills.
    - Reward strong action-oriented bullets.
    - Reward measurable achievements.
    - Reward technical implementation.
    - Avoid rewarding keyword stuffing or excessive resume length.
    """

    text = resume_text or ""
    text_lower = text.lower()

    breakdown = {}
    suggestions = []
    score = 0

    # ============================================================
    # 1. CONTACT & HEADER — 10
    # ============================================================

    contact_score = 0

    if resume_info.get("name"):
        contact_score += 4

    if resume_info.get("email"):
        contact_score += 3

    if resume_info.get("phone"):
        contact_score += 3

    breakdown["contact"] = contact_score
    score += contact_score

    if contact_score < 10:
        suggestions.append(
            "Complete the resume header with your name, professional "
            "email, and phone number."
        )

    # ============================================================
    # 2. SKILLS & KEYWORD QUALITY — 20
    # ============================================================

    skills = resume_info.get("skills", [])

    raw_skills = [
        skill.strip()
        for skill in skills
        if isinstance(skill, str) and skill.strip()
    ]

    normalized_skills = {
        _normalize_skill(skill)
        for skill in raw_skills
    }

    skill_score = 0

    # ------------------------------------------------------------
    # Meaningful technical breadth — 6 points
    # ------------------------------------------------------------

    technical_keywords = {
        "python",
        "java",
        "c++",
        "javascript",
        "typescript",
        "react",
        "fastapi",
        "node",
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "machine learning",
        "artificial intelligence",
        "scikit-learn",
        "pandas",
        "numpy",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "gcp",
        "tensorflow",
        "pytorch",
        "power bi",
        "rest apis",
    }

    technical_skills = normalized_skills.intersection(
        technical_keywords
    )

    technical_count = len(technical_skills)

    if technical_count >= 8:
        skill_score += 6
    elif technical_count >= 5:
        skill_score += 5
    elif technical_count >= 3:
        skill_score += 3
    elif technical_count >= 1:
        skill_score += 1

    # ------------------------------------------------------------
    # Skill diversity — 5 points
    # ------------------------------------------------------------

    categories = {
        "languages": {
            "python",
            "java",
            "c++",
            "javascript",
            "typescript",
            "sql",
        },
        "frameworks": {
            "react",
            "fastapi",
            "node",
            "tensorflow",
            "pytorch",
        },
        "data_ml": {
            "machine learning",
            "artificial intelligence",
            "scikit-learn",
            "pandas",
            "numpy",
            "power bi",
        },
        "tools_cloud": {
            "git",
            "github",
            "docker",
            "aws",
            "azure",
            "gcp",
            "postman",
        },
        "databases": {
            "mysql",
            "postgresql",
            "mongodb",
        },
    }

    category_count = sum(
        1
        for category_skills in categories.values()
        if normalized_skills.intersection(category_skills)
    )

    if category_count >= 4:
        skill_score += 5
    elif category_count == 3:
        skill_score += 4
    elif category_count == 2:
        skill_score += 2
    elif category_count == 1:
        skill_score += 1

    # ------------------------------------------------------------
    # Skills used in actual resume content — 5 points
    # ------------------------------------------------------------

    implementation_matches = 0

    if text:
        for skill in technical_skills:
            if re.search(
                r"\b" + re.escape(skill) + r"\b",
                text_lower,
                re.IGNORECASE
            ):
                implementation_matches += 1

    if implementation_matches >= 6:
        skill_score += 5
    elif implementation_matches >= 4:
        skill_score += 4
    elif implementation_matches >= 2:
        skill_score += 2
    elif implementation_matches >= 1:
        skill_score += 1

    # ------------------------------------------------------------
    # Duplicate / overlapping skills — 4 points
    # ------------------------------------------------------------

    duplicate_groups = []

    raw_skill_set = {
        skill.lower()
        for skill in raw_skills
    }

    # True duplicate variants
    if (
        "react" in raw_skill_set
        and "react.js" in raw_skill_set
    ):
        duplicate_groups.append(
            "React / React.js"
        )

    if (
        "reactjs" in raw_skill_set
        and (
            "react" in raw_skill_set
            or "react.js" in raw_skill_set
        )
    ):
        duplicate_groups.append(
            "React / ReactJS"
        )

    # Git / GitHub and SQL / MySQL are related,
    # but they are NOT treated as duplicates.

    if not duplicate_groups:
        skill_score += 4

    elif len(duplicate_groups) == 1:
        skill_score += 2

        suggestions.append(
            "Consolidate duplicate skill variants: "
            + ", ".join(duplicate_groups)
            + "."
        )

    else:
        skill_score += 0

        suggestions.append(
            "Remove or consolidate duplicate skill variants: "
            + ", ".join(duplicate_groups)
            + "."
        )

    skill_score = min(skill_score, 20)

    breakdown["skills"] = skill_score
    score += skill_score

    # ============================================================
    # 3. EDUCATION — 10
    # ============================================================

    education = resume_info.get("education", [])

    education_score = 0

    if education:
        education_score += 5

    degree_text = " ".join(
        item.get("degree", "")
        for item in education
        if isinstance(item, dict)
    )

    institution_text = " ".join(
        item.get("institution", "")
        for item in education
        if isinstance(item, dict)
    )

    if degree_text:
        education_score += 3

    if institution_text:
        education_score += 2

    education_score = min(education_score, 10)

    breakdown["education"] = education_score
    score += education_score

    if not education:
        suggestions.append(
            "Add a clearly formatted Education section."
        )

    # Detect potentially unclear future education dates.
    future_year_pattern = re.search(
        r"(20\d{2})\s*[-–]\s*(20\d{2})",
        text
    )

    if future_year_pattern:
        if not _contains_any(
            text,
            [
                "expected",
                "incoming",
                "anticipated",
                "candidate for",
            ]
        ):
            suggestions.append(
                "Clearly label future or ongoing degrees as "
                "'Expected', 'Incoming', or 'Anticipated' "
                "to avoid timeline confusion."
            )

    # ============================================================
    # 4. EXPERIENCE QUALITY — 20
    # ============================================================

    experience = resume_info.get("experience", [])

    experience_score = 0

    experience_descriptions = _collect_text(
        experience,
        "description"
    )

    experience_text = " ".join(
        experience_descriptions
    )

    if experience:
        # Existence — 3 points
        experience_score += 3

        # --------------------------------------------------------
        # Action verbs — 5 points
        # --------------------------------------------------------

        action_verbs = [
            "built",
            "developed",
            "designed",
            "implemented",
            "engineered",
            "created",
            "analyzed",
            "optimized",
            "managed",
            "improved",
            "automated",
            "deployed",
            "integrated",
            "streamlined",
            "configured",
            "tested",
            "maintained",
        ]

        action_count = _count_matches(
            experience_text,
            action_verbs
        )

        if action_count >= 5:
            experience_score += 5
        elif action_count >= 3:
            experience_score += 4
        elif action_count >= 2:
            experience_score += 2
        elif action_count >= 1:
            experience_score += 1

        # --------------------------------------------------------
        # Quantified achievements — 4 points
        # --------------------------------------------------------

        quantified_items = sum(
            1
            for description in experience_descriptions
            if re.search(
                r"\d+(?:\.\d+)?[%+]?",
                description
            )
        )

        if quantified_items >= 3:
            experience_score += 4
        elif quantified_items >= 2:
            experience_score += 3
        elif quantified_items >= 1:
            experience_score += 1

        # --------------------------------------------------------
        # Technical contribution — 5 points
        # --------------------------------------------------------

        technical_terms = [
            "python",
            "java",
            "javascript",
            "react",
            "fastapi",
            "sql",
            "mysql",
            "machine learning",
            "artificial intelligence",
            "software",
            "api",
            "database",
            "programming",
            "development",
            "data",
            "automation",
            "analysis",
            "engineering",
        ]

        technical_matches = _count_matches(
            experience_text,
            technical_terms
        )

        if technical_matches >= 5:
            experience_score += 5
        elif technical_matches >= 3:
            experience_score += 3
        elif technical_matches >= 1:
            experience_score += 1

        # --------------------------------------------------------
        # Bullet quality — 3 points
        # --------------------------------------------------------

        weak_verbs = [
            "observed",
            "learned",
            "gained",
            "attended",
            "participated",
            "completed",
            "exposed",
            "studied",
        ]

        weak_count = _count_matches(
            experience_text,
            weak_verbs
        )

        if weak_count == 0 and action_count >= 2:
            experience_score += 3
        elif weak_count <= 1:
            experience_score += 1

        if weak_count >= 2:
            suggestions.append(
                "Replace passive experience wording such as "
                "'observed', 'learned', or 'gained exposure' "
                "with specific contributions, actions, and outcomes."
            )

    else:
        suggestions.append(
            "Add internships, employment, freelance work, "
            "or other relevant practical experience."
        )

    experience_score = min(
        experience_score,
        20
    )

    breakdown["experience"] = experience_score
    score += experience_score

    if experience and experience_score < 12:
        suggestions.append(
            "Strengthen experience bullets with technical "
            "contributions, strong action verbs, and measurable outcomes."
        )

    # ============================================================
    # 5. PROJECTS — 15
    # ============================================================

    projects = resume_info.get("projects", [])

    project_score = 0

    project_descriptions = _collect_text(
        projects,
        "description"
    )

    project_technologies = []

    for project in projects:
        if not isinstance(project, dict):
            continue

        technologies = project.get(
            "technologies",
            []
        )

        if isinstance(technologies, list):
            project_technologies.extend(
                technology
                for technology in technologies
                if isinstance(technology, str)
            )

    unique_technologies = {
        technology.strip().lower()
        for technology in project_technologies
        if technology.strip()
    }

    if len(projects) >= 3:
        project_score += 4
    elif len(projects) == 2:
        project_score += 3
    elif len(projects) == 1:
        project_score += 2

    # Technical implementation — 4 points
    if len(unique_technologies) >= 6:
        project_score += 4
    elif len(unique_technologies) >= 4:
        project_score += 3
    elif len(unique_technologies) >= 2:
        project_score += 2
    elif unique_technologies:
        project_score += 1

    # Action-oriented project descriptions — 3 points
    project_text = " ".join(
        project_descriptions
    )

    project_action_count = _count_matches(
        project_text,
        [
            "built",
            "developed",
            "designed",
            "implemented",
            "engineered",
            "created",
            "optimized",
            "deployed",
            "integrated",
            "automated",
        ]
    )

    if project_action_count >= 5:
        project_score += 3
    elif project_action_count >= 3:
        project_score += 2
    elif project_action_count >= 1:
        project_score += 1

    # Quantified outcomes — 4 points
    quantified_projects = sum(
        1
        for description in project_descriptions
        if re.search(
            r"\d+(?:\.\d+)?[%+]?",
            description
        )
    )

    if quantified_projects >= 4:
        project_score += 4
    elif quantified_projects >= 2:
        project_score += 3
    elif quantified_projects == 1:
        project_score += 1

    project_score = min(
        project_score,
        15
    )

    breakdown["projects"] = project_score
    score += project_score

    if projects and project_score < 10:
        suggestions.append(
            "Strengthen project descriptions with specific "
            "technical implementations, actions, and measurable outcomes."
        )

    if not projects:
        suggestions.append(
            "Add technical projects demonstrating practical skills."
        )

    # ============================================================
    # 6. CONTENT & BULLET QUALITY — 15
    # ============================================================

    content_score = 0

    if text:

        # --------------------------------------------------------
        # Professional summary — 3 points
        # --------------------------------------------------------

        summary_patterns = [
            r"\bprofessional summary\b",
            r"\bsummary\b",
            r"\bprofile\b",
            r"\bobjective\b",
        ]

        if any(
            re.search(
                pattern,
                text_lower
            )
            for pattern in summary_patterns
        ):
            content_score += 3
        else:
            suggestions.append(
                "Add a concise professional summary targeted "
                "to your desired technical role."
            )

        # --------------------------------------------------------
        # Action-oriented language — 4 points
        # --------------------------------------------------------

        all_action_verbs = [
            "built",
            "developed",
            "designed",
            "implemented",
            "engineered",
            "created",
            "analyzed",
            "optimized",
            "managed",
            "improved",
            "automated",
            "deployed",
            "integrated",
            "streamlined",
            "configured",
            "tested",
            "maintained",
        ]

        action_count = _count_matches(
            text,
            all_action_verbs
        )

        if action_count >= 8:
            content_score += 4
        elif action_count >= 5:
            content_score += 3
        elif action_count >= 2:
            content_score += 2
        elif action_count >= 1:
            content_score += 1

        # --------------------------------------------------------
        # Quantification — 4 points
        # --------------------------------------------------------

        numbers = re.findall(
            r"\b\d+(?:\.\d+)?[%+]?\b",
            text
        )

        if len(numbers) >= 8:
            content_score += 4
        elif len(numbers) >= 5:
            content_score += 3
        elif len(numbers) >= 3:
            content_score += 2
        elif len(numbers) >= 1:
            content_score += 1

        # --------------------------------------------------------
        # Readability / repetition — 4 points
        # --------------------------------------------------------

        words = re.findall(
            r"\b[a-zA-Z]{3,}\b",
            text_lower
        )

        if words:
            word_counts = {}

            for word in words:
                word_counts[word] = (
                    word_counts.get(word, 0) + 1
                )

            repeated_words = [
                word
                for word, count in word_counts.items()
                if count >= 8
                and word not in {
                    "with",
                    "from",
                    "using",
                    "project",
                    "developed",
                    "experience",
                    "skills",
                }
            ]

            if len(repeated_words) <= 3:
                content_score += 4
            elif len(repeated_words) <= 6:
                content_score += 2
            else:
                content_score += 0

                suggestions.append(
                    "Review repetitive wording and avoid repeating "
                    "the same technical terms across multiple bullets."
                )

    else:
        content_score += 5

    content_score = min(
        content_score,
        15
    )

    breakdown["content_quality"] = content_score
    score += content_score

    # ============================================================
    # 7. ATS STRUCTURE & READABILITY — 10
    # ============================================================

    structure_score = 0

    if text:

        sections = {
            "skills": r"\bskills\b",
            "education": r"\beducation\b",
            "experience": r"\bexperience\b",
            "projects": r"\bprojects\b",
        }

        detected_sections = sum(
            1
            for pattern in sections.values()
            if re.search(
                pattern,
                text_lower
            )
        )

        if detected_sections == 4:
            structure_score += 5
        elif detected_sections == 3:
            structure_score += 4
        elif detected_sections == 2:
            structure_score += 3
        elif detected_sections == 1:
            structure_score += 1

        # Contact information
        if (
            resume_info.get("email")
            and resume_info.get("phone")
        ):
            structure_score += 2

        # Reasonable skill count
        skill_count = len(normalized_skills)

        if 5 <= skill_count <= 20:
            structure_score += 2
        elif 21 <= skill_count <= 25:
            structure_score += 1
        elif skill_count > 25:
            suggestions.append(
                "Reduce the skills list to technologies that are "
                "genuinely relevant to your target roles."
            )

        # Detect extremely long text.
        word_count = len(text.split())

        if word_count <= 1000:
            structure_score += 1
        else:
            suggestions.append(
                "Reduce unnecessary resume content and keep the "
                "document concise and easy to scan."
            )

    else:
        structure_score += 5

    structure_score = min(
        structure_score,
        10
    )

    breakdown["ats_structure"] = structure_score
    score += structure_score

    # ============================================================
    # FINAL RESULT
    # ============================================================

    score = min(
        round(score),
        100
    )

    # Remove duplicate suggestions while preserving order.
    unique_suggestions = []

    for suggestion in suggestions:
        if suggestion not in unique_suggestions:
            unique_suggestions.append(suggestion)

    return {
        "ats_score": score,
        "max_score": 100,
        "breakdown": breakdown,
        "suggestions": unique_suggestions,
    }