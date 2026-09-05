from services.resume_parser import extract_text_from_pdf
from services.resume_extractor import extract_resume
from services.ai_resume_review import review_resume

PDF_PATH = "../uploads/Resume.pdf"

text = extract_text_from_pdf(PDF_PATH)

resume = extract_resume(text)

review = review_resume(resume)

print(review)