from dotenv import load_dotenv
from fastapi import FastAPI
from api.upload import router as upload_router
from api.ats import router as ats_router
from api.job_match import router as job_match_router
from api.ai_review import router as ai_router
from api.analyze import router as analyze_router
from api.improve_resume import router as improve_resume_router
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend API for Resume Analyzer & ATS Optimizer",
    version="1.0.0"
)

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

frontend_url = os.getenv("FRONTEND_URL")

if frontend_url:
    allowed_origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)
app.include_router(ats_router)
app.include_router(job_match_router)
app.include_router(ai_router, tags=["AI Review"])
app.include_router(analyze_router, tags=["Analyze Resume"])
app.include_router(improve_resume_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }