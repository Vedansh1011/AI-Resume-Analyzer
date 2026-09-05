from pprint import pprint

from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.ats_service import calculate_ats_score

PDF_PATH = "../uploads/Resume.pdf"

text = extract_text_from_pdf(PDF_PATH)

resume = extract_resume(text)

ats_result = calculate_ats_score(resume, text)

print("\n" + "=" * 60)
print("ATS RESULT")
print("=" * 60)

pprint(ats_result)

print("\nSuggestions:")

for suggestion in ats_result["suggestions"]:
    print(f"• {suggestion}")