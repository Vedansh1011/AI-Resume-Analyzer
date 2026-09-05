import json

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.resume_improver import improve_resume


PDF_PATH = "../uploads/Resume.pdf"


def main():

    print("=" * 60)
    print("IMPROVE RESUME API LOGIC TEST")
    print("=" * 60)

    # Extract resume text
    text = extract_text_from_pdf(PDF_PATH)

    # Convert to structured resume data
    resume_data = extract_resume(text)

    print("\nResume extracted successfully.")

    # Run the same service used by the API endpoint
    result = improve_resume(resume_data)

    print("\nResume improvement generated successfully.")

    print("\n" + "=" * 60)
    print("API RESPONSE")
    print("=" * 60)

    print(
        json.dumps(
            {
                "success": True,
                "improvement": result
            },
            indent=2,
            ensure_ascii=False
        )
    )


if __name__ == "__main__":
    main()