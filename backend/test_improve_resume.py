from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.resume_improver import improve_resume


PDF_PATH = "../uploads/Resume.pdf"


def main():

    print("\n" + "=" * 60)
    print("RESUME IMPROVEMENT TEST")
    print("=" * 60)

    # Extract text from the PDF
    text = extract_text_from_pdf(PDF_PATH)

    # Convert extracted text into structured resume data
    resume_data = extract_resume(text)

    # Send structured resume data to Gemini
    result = improve_resume(resume_data)

    print("\n" + "=" * 60)
    print("PROFESSIONAL SUMMARY")
    print("=" * 60)

    summary = result.get("professional_summary", {})

    print("\nOriginal:")
    print(summary.get("original", ""))

    print("\nImproved:")
    print(summary.get("improved", ""))


    print("\n" + "=" * 60)
    print("EDUCATION IMPROVEMENTS")
    print("=" * 60)

    for item in result.get("education_improvements", []):

        print("\nOriginal:")
        print(item.get("original", ""))

        print("\nImproved:")
        print(item.get("improved", ""))

        print("\nReason:")
        print(item.get("reason", ""))


    print("\n" + "=" * 60)
    print("EXPERIENCE IMPROVEMENTS")
    print("=" * 60)

    for item in result.get("experience_improvements", []):

        print(f"\nSection: {item.get('section', '')}")

        print("\nBefore:")
        print(item.get("original", ""))

        print("\nAfter:")
        print(item.get("improved", ""))

        print("\nReason:")
        print(item.get("reason", ""))


    print("\n" + "=" * 60)
    print("PROJECT IMPROVEMENTS")
    print("=" * 60)

    for item in result.get("project_improvements", []):

        print(f"\nProject: {item.get('project', '')}")

        print("\nBefore:")
        print(item.get("original", ""))

        print("\nAfter:")
        print(item.get("improved", ""))

        print("\nReason:")
        print(item.get("reason", ""))


    print("\n" + "=" * 60)
    print("SKILLS IMPROVEMENTS")
    print("=" * 60)

    skills = result.get("skills_improvements", {})

    print("\nDuplicates to Remove:")

    for skill in skills.get("duplicates_to_remove", []):
        print(f"• {skill}")


    print("\nRecommended Skills Structure:")

    structure = skills.get("recommended_structure", {})

    for category, values in structure.items():

        print(f"\n{category}:")

        for value in values:
            print(f"• {value}")


    print("\nSkills Notes:")

    for note in skills.get("notes", []):
        print(f"• {note}")


    print("\n" + "=" * 60)
    print("READABILITY IMPROVEMENTS")
    print("=" * 60)

    for item in result.get("readability_improvements", []):
        print(f"• {item}")


    print("\n" + "=" * 60)
    print("ATS IMPROVEMENTS")
    print("=" * 60)

    for item in result.get("ats_improvements", []):
        print(f"• {item}")


    print("\n" + "=" * 60)
    print("IMPORTANT NOTES")
    print("=" * 60)

    for item in result.get("important_notes", []):
        print(f"• {item}")


if __name__ == "__main__":
    main()