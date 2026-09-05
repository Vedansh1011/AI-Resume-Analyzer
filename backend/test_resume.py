from pprint import pprint

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume

PDF_PATH = "../uploads/Resume.pdf"


def main():

    text = extract_text_from_pdf(PDF_PATH)

    resume = extract_resume(text)

    print("\n" + "=" * 60)
    print("EXTRACTED RESUME")
    print("=" * 60)

    pprint(resume)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(f"Name       : {resume['name']}")
    print(f"Email      : {resume['email']}")
    print(f"Phone      : {resume['phone']}")
    print(f"Skills     : {len(resume['skills'])}")
    print(f"Education  : {len(resume['education'])}")
    print(f"Experience : {len(resume['experience'])}")
    print(f"Projects   : {len(resume['projects'])}")


if __name__ == "__main__":
    main()