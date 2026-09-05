# AI Resume Analyzer

AI Resume Analyzer is a full-stack AI-powered web application designed to analyze resumes, evaluate ATS compatibility, provide AI-generated resume feedback, match resumes against job descriptions, and generate actionable resume improvement recommendations.

The application combines PDF text extraction, resume parsing, text processing, ATS-oriented analysis, job-description processing, and Generative AI to provide practical resume insights through a production-deployed web interface.

---

## Live Demo

### Web Application

https://ai-resume-analyzer-eight-lilac.vercel.app

### Backend API

https://ai-resume-analyzer-43et.onrender.com

### GitHub Repository

https://github.com/Vedansh1011/AI-Resume-Analyzer

---

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Application Workflow](#application-workflow)
- [AI Processing Pipeline](#ai-processing-pipeline)
- [Backend Architecture](#backend-architecture)
- [Frontend Architecture](#frontend-architecture)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [API Overview](#api-overview)
- [Resume Processing](#resume-processing)
- [ATS Analysis](#ats-analysis)
- [AI Resume Review](#ai-resume-review)
- [Job Description Matching](#job-description-matching)
- [Resume Improvement](#resume-improvement)
- [Google Gemini Integration](#google-gemini-integration)
- [Configuration](#configuration)
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
- [CORS Configuration](#cors-configuration)
- [Testing and Validation](#testing-and-validation)
- [Engineering Design Decisions](#engineering-design-decisions)
- [Security Considerations](#security-considerations)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Roadmap](#roadmap)
- [Technical Skills Demonstrated](#technical-skills-demonstrated)
- [Project Outcomes](#project-outcomes)
- [Author](#author)
- [License](#license)

---

## Project Overview

Recruitment systems increasingly use automated resume screening and Applicant Tracking Systems (ATS) to evaluate candidates.

Candidates commonly face difficulties such as:

- Understanding whether their resume is ATS-friendly.
- Identifying weaknesses in resume content.
- Knowing which skills and keywords are relevant to a target role.
- Aligning a resume with a specific job description.
- Improving the clarity and effectiveness of resume content.
- Receiving structured feedback without manually reviewing every resume section.

AI Resume Analyzer addresses these problems through a single full-stack application.

A user can upload a PDF resume and use the application to:

1. Extract and process resume content.
2. Parse and validate resume information.
3. Analyze the resume.
4. Generate an ATS-oriented score.
5. Receive an AI-powered resume review.
6. Compare the resume with a job description.
7. Identify matching and potentially missing skills.
8. Receive actionable resume improvement recommendations.

The application is designed as a modular system with a React frontend, FastAPI backend, dedicated processing services, and Google Gemini integration.

---

## Problem Statement

Traditional resume evaluation can be time-consuming and subjective.

A candidate may need to manually determine:

- Whether important information is present.
- Whether the resume contains relevant keywords.
- Whether the resume aligns with a specific job description.
- Which skills are missing.
- Which sections require improvement.
- How to rewrite weak resume content.

At the same time, automated recruitment systems may evaluate resumes using criteria that are not always visible to candidates.

The objective of this project is to build an accessible AI-powered platform that provides structured resume analysis and practical recommendations.

---

## Objectives

The primary objectives of the project are:

1. Build a practical AI-powered resume analysis platform.
2. Extract useful information from PDF resumes.
3. Parse and validate resume content.
4. Perform ATS-oriented resume evaluation.
5. Generate a structured ATS score.
6. Provide AI-powered resume feedback.
7. Compare resumes against target job descriptions.
8. Identify matching and potentially missing skills.
9. Provide resume improvement recommendations.
10. Develop a modular backend architecture.
11. Build a responsive web-based frontend.
12. Deploy the complete application to production.

---

# Key Features

## 1. Resume Upload

Users can upload their resume in PDF format through the web application.

The uploaded document is sent to the FastAPI backend for processing.

### Processing Flow

```text
PDF Resume
    |
    v
Resume Upload
    |
    v
FastAPI Backend
    |
    v
PDF Text Extraction
    |
    v
Text Processing
    |
    v
Resume Parsing
    |
    v
Resume Analysis
```

---

## 2. ATS Analysis

The application provides ATS-oriented analysis of the uploaded resume.

The ATS analysis produces an overall score and identifies areas where the resume can potentially be improved.

The analysis considers resume content and provides observations related to areas such as:

- Resume quality
- Relevant content
- Keywords
- Skills
- Experience
- Resume structure
- Potential improvement areas

The ATS score is an analytical approximation and should not be interpreted as the exact score produced by any proprietary recruitment platform.

---

## 3. AI Resume Review

The application uses Google's Gemini API to generate AI-powered resume feedback.

The AI review can evaluate areas such as:

- Resume strengths
- Resume weaknesses
- Professional summary
- Technical skills
- Experience
- Education
- Potentially missing information
- Relevant keywords
- Overall resume quality
- Improvement recommendations

The generated AI response is processed into a structured format before being returned to the frontend.

---

## 4. Job Description Matching

Users can provide a target job description and compare it against their resume.

The application analyzes the relationship between the resume and job requirements.

The job matching functionality can provide:

- Job match score
- Matching skills
- Potentially missing skills
- Relevant keywords
- Role compatibility observations
- Improvement recommendations

### Job Matching Flow

```text
Resume
   |
   v
Resume Processing
   |
   v
Resume Skills and Keywords
   |
   |-----------------------------|
                                 |
                                 v
                         Job Description
                                 |
                                 v
                         JD Processing
                                 |
                                 v
                       Skill Extraction
                                 |
                                 v
                       Skill Comparison
                                 |
                                 v
                         Match Analysis
                                 |
                                 v
                        Recommendations
```

---

## 5. Resume Improvement

The application provides AI-assisted resume improvement recommendations.

The objective is to help users improve:

- Content clarity
- Professional wording
- Keyword relevance
- Resume effectiveness
- Job-specific alignment
- Overall presentation

The improvement functionality focuses on actionable recommendations that users can apply to their resume.

---

# System Architecture

The project follows a separated frontend-backend architecture.

```text
                         USER
                           |
                           v
                React + Vite Frontend
                        Vercel
                           |
                           | HTTP / REST API
                           v
                    FastAPI Backend
                        Render
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
      Resume Processing  ATS Analysis  Job Matching
             |             |             |
             +-------------+-------------+
                           |
                           v
                    AI Resume Review
                           |
                           v
                   Google Gemini API
                           |
                           v
                  Structured AI Results
                           |
                           v
                    React Frontend
```

---

# Application Workflow

The complete application workflow is:

```text
User
 |
 v
Upload Resume
 |
 v
Frontend Validation
 |
 v
FastAPI API
 |
 v
PDF Text Extraction
 |
 v
Text Cleaning
 |
 v
Resume Parsing
 |
 v
Resume Validation
 |
 +----------------------+----------------------+
 |                      |                      |
 v                      v                      v
ATS Analysis       AI Resume Review      Resume Analysis
 |                      |                      |
 |                      v                      |
 |                Gemini API                   |
 |                      |                      |
 +----------------------+----------------------+
                        |
                        v
                Structured Results
                        |
                        v
                 React Frontend
                        |
                        v
                    User View
```

---

# AI Processing Pipeline

The resume analysis pipeline combines deterministic processing with Generative AI.

```text
PDF Resume
    |
    v
Upload
    |
    v
PDF Text Extraction
    |
    v
Text Cleaning
    |
    v
Resume Parsing
    |
    v
Resume Validation
    |
    +---------------------+
    |                     |
    v                     v
ATS Analysis         AI Resume Review
    |                     |
    |                     v
    |               Gemini API
    |                     |
    +----------+----------+
               |
               v
       Structured Results
               |
               v
        Frontend Display
```

This approach separates document processing from AI-based interpretation.

---

# Backend Architecture

The backend is implemented using FastAPI and follows a layered architecture.

```text
API Route
    |
    v
Schema / Validation
    |
    v
Service Layer
    |
    v
Processing / AI Logic
    |
    v
Structured Response
```

The backend is divided into:

```text
API Layer
    |
    v
Schema Layer
    |
    v
Service Layer
    |
    v
Utility Layer
```

This separation keeps HTTP handling, validation, business logic, and utility functionality independent.

---

## API Layer

Location:

```text
backend/api/
```

The API layer contains FastAPI route implementations.

Current modules include:

```text
ai_review.py
analyze.py
ats.py
improve_resume.py
job_match.py
upload.py
```

Responsibilities include:

- Receiving HTTP requests.
- Handling uploaded files.
- Validating request data.
- Calling service-layer functionality.
- Returning structured responses.

---

## Schema Layer

Location:

```text
backend/schemas/
```

Current modules include:

```text
job_description_schema.py
resume_schema.py
```

The schema layer provides structured validation for application data.

---

## Service Layer

Location:

```text
backend/services/
```

The service layer contains the main processing and business logic.

Current services include:

```text
ai_resume_review.py
ats_service.py
jd_matcher.py
jd_skill_extractor.py
resume_extractor.py
resume_improver.py
resume_parser.py
resume_validator.py
role_analysis_service.py
```

Responsibilities include:

- Resume extraction
- Resume parsing
- Resume validation
- ATS analysis
- Job-description processing
- Skill extraction
- Job matching
- AI resume review
- Resume improvement
- Role analysis

---

## Utility Layer

Location:

```text
backend/utils/
```

Current utilities include:

```text
logger.py
text_cleaner.py
```

These modules provide reusable functionality for logging and text processing.

---

# Frontend Architecture

The frontend is developed using React and Vite.

The primary component flow is:

```text
main.jsx
    |
    v
App.jsx
    |
    v
Home.jsx
    |
    +--------------------+
    |                    |
    v                    v
Navbar              UploadCard
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
          ATSCard   AIReviewCard  JobMatchCard
                                     |
                                     v
                              ImproveResumeCard
                                     |
                                     v
                                  api.js
                                     |
                                     v
                              FastAPI Backend
```

The frontend is responsible for:

- User interface rendering.
- Resume upload.
- User interaction.
- Job description input.
- API communication.
- ATS result presentation.
- AI review presentation.
- Job match presentation.
- Resume improvement presentation.

---

# Project Structure

```text
AI-Resume-Analyzer/
|
+-- backend/
|   |
|   +-- app.py
|   |
|   +-- api/
|   |   +-- ai_review.py
|   |   +-- analyze.py
|   |   +-- ats.py
|   |   +-- improve_resume.py
|   |   +-- job_match.py
|   |   +-- upload.py
|   |
|   +-- schemas/
|   |   +-- job_description_schema.py
|   |   +-- resume_schema.py
|   |
|   +-- services/
|   |   +-- ai_resume_review.py
|   |   +-- ats_service.py
|   |   +-- jd_matcher.py
|   |   +-- jd_skill_extractor.py
|   |   +-- resume_extractor.py
|   |   +-- resume_improver.py
|   |   +-- resume_parser.py
|   |   +-- resume_validator.py
|   |   +-- role_analysis_service.py
|   |
|   +-- utils/
|   |   +-- logger.py
|   |   +-- text_cleaner.py
|   |
|   +-- requirements.txt
|   +-- .env
|
+-- frontend/
|   |
|   +-- public/
|   |   +-- favicon.svg
|   |
|   +-- src/
|       |
|       +-- main.jsx
|       +-- App.jsx
|       +-- index.css
|       |
|       +-- pages/
|       |   +-- Home.jsx
|       |
|       +-- components/
|       |   +-- Navbar.jsx
|       |   +-- UploadCard.jsx
|       |   +-- ATSCard.jsx
|       |   +-- AIReviewCard.jsx
|       |   +-- JobMatchCard.jsx
|       |   +-- ImproveResumeCard.jsx
|       |
|       +-- services/
|           +-- api.js
|   |
|   +-- package.json
|   +-- package-lock.json
|   +-- vite.config.js
|   +-- eslint.config.js
|
+-- uploads/
+-- venv/
+-- .gitignore
+-- README.md
```

The following resources are local/runtime resources and are excluded from version control:

```text
.env
uploads/
venv/
frontend/node_modules/
frontend/dist/
Python cache files
```

---

# Technology Stack

## Frontend

| Technology | Purpose |
|---|---|
| React | User interface |
| Vite | Frontend development and build tooling |
| JavaScript | Application logic |
| Axios | HTTP/API communication |
| CSS | User interface styling |

## Backend

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| Pydantic | Data validation |
| PyMuPDF | PDF text extraction |
| python-dotenv | Environment configuration |

## Artificial Intelligence

| Technology | Purpose |
|---|---|
| Google Gemini API | Generative AI processing |
| Gemini 3.5 Flash | AI model used for resume analysis |

## Development and Deployment

| Technology | Purpose |
|---|---|
| Git | Version control |
| GitHub | Source code hosting |
| Vercel | Frontend deployment |
| Render | Backend deployment |

---

# API Overview

The FastAPI backend provides APIs for the application's core functionality.

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | API welcome endpoint |
| `/health` | GET | Backend health check |
| `/analyze-resume` | POST | Analyze an uploaded resume |
| Upload API | POST | Process uploaded resume |
| ATS API | POST | Perform ATS analysis |
| AI Review API | POST | Generate AI-powered resume review |
| Job Match API | POST | Compare resume with job description |
| Improve Resume API | POST | Generate resume improvement recommendations |

The actual API implementations are located in:

```text
backend/api/
```

---

# Resume Processing

Resume processing is one of the core components of the application.

The processing pipeline includes:

```text
PDF
 |
 v
Text Extraction
 |
 v
Text Cleaning
 |
 v
Resume Parsing
 |
 v
Resume Validation
 |
 v
Structured Resume Information
```

The application uses PyMuPDF for PDF text extraction.

After extraction, the text is processed by dedicated backend services before being passed to downstream analysis components.

---

# ATS Analysis

The ATS analysis functionality is implemented through a dedicated service.

The general workflow is:

```text
Resume
   |
   v
Text Extraction
   |
   v
Text Processing
   |
   v
Resume Content Analysis
   |
   v
ATS Evaluation
   |
   v
ATS Score
   |
   v
Recommendations
```

The ATS analysis is intended to provide an approximate assessment based on implemented analysis logic.

It does not reproduce the proprietary scoring algorithm of any specific ATS provider.

---

# AI Resume Review

The AI Resume Review functionality uses Google's Gemini API.

The general workflow is:

```text
Resume Information
       |
       v
Prompt Construction
       |
       v
Gemini API
       |
       v
Generated AI Response
       |
       v
Response Processing
       |
       v
Structured AI Review
       |
       v
Frontend
```

The AI review can provide structured feedback related to:

- Strengths
- Weaknesses
- Skills
- Experience
- Education
- Resume quality
- Potential keywords
- Improvement recommendations

---

# Job Description Matching

The job matching workflow compares resume information with a target job description.

```text
Resume
   |
   v
Resume Processing
   |
   v
Resume Skills / Keywords
   |
   +-----------------------------+
                                 |
                                 v
                         Job Description
                                 |
                                 v
                          JD Processing
                                 |
                                 v
                         Skill Extraction
                                 |
                                 v
                         Skill Comparison
                                 |
                                 v
                           Match Analysis
                                 |
                                 v
                          Recommendations
```

The system can identify:

- Matching skills
- Potentially missing skills
- Relevant keywords
- Job compatibility observations
- Areas for improvement

---

# Resume Improvement

The resume improvement functionality provides recommendations based on the analyzed resume.

The objective is to improve the effectiveness of resume content.

Potential improvement areas include:

- Content clarity
- Professional wording
- Keyword relevance
- Role alignment
- Resume effectiveness
- Presentation

The functionality is implemented through a dedicated backend service and exposed through the frontend.

---

# Google Gemini Integration

Google Gemini provides the Generative AI capabilities used by the application.

The backend uses the Google GenAI Python SDK.

The Gemini client is configured using environment variables.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash
```

The AI workflow is:

```text
Resume Data
     |
     v
Prompt
     |
     v
Gemini Model
     |
     v
Generated Response
     |
     v
Response Parsing
     |
     v
Structured Application Data
```

The API key is never stored directly in the source code.

---

# Configuration

The application uses environment variables for secrets and deployment-specific configuration.

## Backend Environment Variables

For local development:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash
FRONTEND_URL=http://localhost:5173
```

For production:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash
FRONTEND_URL=https://ai-resume-analyzer-eight-lilac.vercel.app
PYTHON_VERSION=3.12.10
```

## Frontend Environment Variable

For local development:

```env
VITE_API_URL=http://127.0.0.1:8000
```

For production:

```env
VITE_API_URL=https://ai-resume-analyzer-43et.onrender.com
```

Never commit real API keys or secrets to GitHub.

---

# Local Development

## Prerequisites

Install the following:

- Python 3.12
- Node.js
- npm
- Git

---

## 1. Clone the Repository

```bash
git clone git@github.com:Vedansh1011/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

---

## 2. Create the Python Virtual Environment

From the project root:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

Move into the backend directory:

```powershell
cd backend
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

---

## 4. Configure Backend Environment

Create:

```text
backend/.env
```

Add:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash
FRONTEND_URL=http://localhost:5173
```

Replace `your_gemini_api_key` with your actual Gemini API key.

Do not commit the `.env` file.

---

## 5. Start the Backend

From the `backend` directory:

```powershell
uvicorn app:app --host 127.0.0.1 --port 8000
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

---

## 6. Install Frontend Dependencies

Open another terminal.

From the project root:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

---

## 7. Start the Frontend

```powershell
npm run dev
```

The Vite development server will normally be available at:

```text
http://localhost:5173
```

---

# Production Deployment

The project uses separate production deployments for the frontend and backend.

```text
                         GitHub
                           |
             +-------------+-------------+
             |                           |
             v                           v
          Vercel                       Render
             |                           |
             v                           v
       React + Vite                   FastAPI
        Frontend                      Backend
             |                           |
             +-------------+-------------+
                           |
                           v
                     Gemini API
```

---

## Frontend Deployment - Vercel

The React/Vite frontend is deployed on Vercel.

Configuration:

```text
Root Directory: frontend
Framework: Vite
Build Command: npm run build
Output Directory: dist
Install Command: npm install
```

Production URL:

```text
https://ai-resume-analyzer-eight-lilac.vercel.app
```

The frontend communicates with the backend using:

```text
VITE_API_URL
```

Production value:

```text
https://ai-resume-analyzer-43et.onrender.com
```

---

## Backend Deployment - Render

The FastAPI backend is deployed on Render.

Configuration:

```text
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
Python Version: 3.12.10
```

Production URL:

```text
https://ai-resume-analyzer-43et.onrender.com
```

The backend uses environment variables for:

```text
GEMINI_API_KEY
GEMINI_MODEL
FRONTEND_URL
PYTHON_VERSION
```

---

# CORS Configuration

Because the frontend and backend are deployed on separate domains, the FastAPI backend uses Cross-Origin Resource Sharing (CORS) configuration.

Local development origins include:

```text
http://localhost:5173
http://127.0.0.1:5173
```

The production frontend origin is configured through:

```env
FRONTEND_URL=https://ai-resume-analyzer-eight-lilac.vercel.app
```

This allows the deployed React frontend to communicate with the Render backend.

---

# End-to-End Production Flow

A typical production resume analysis request follows this sequence:

```text
1. User opens the Vercel application
              |
              v
2. User uploads a PDF resume
              |
              v
3. React frontend sends API request
              |
              v
4. Render receives request
              |
              v
5. FastAPI processes the request
              |
              v
6. PDF text is extracted
              |
              v
7. Resume is parsed and validated
              |
              v
8. Analysis services execute
              |
              +---- ATS Analysis
              |
              +---- Resume Analysis
              |
              +---- AI Resume Review
              |
              v
9. Gemini API processes AI request
              |
              v
10. Structured response returned
              |
              v
11. React receives the response
              |
              v
12. Results are displayed to the user
```

---

# Testing and Validation

The application has been validated through both local and production workflows.

## Backend Validation

The following areas have been validated:

- FastAPI application startup
- Python compilation
- Dependency installation
- Core dependency imports
- Backend health endpoint
- API root endpoint
- PDF processing
- Resume extraction
- Resume parsing
- Resume validation
- Gemini integration
- ATS analysis
- Job matching
- Resume improvement

---

## Frontend Validation

The following areas have been validated:

- React application startup
- ESLint
- Production build
- API configuration
- Resume upload
- Resume analysis
- ATS result rendering
- AI review rendering
- Job match rendering
- Resume improvement rendering

---

## Production Validation

The deployed application has been validated for:

- Vercel frontend availability
- Render backend availability
- Frontend-to-backend communication
- Production CORS
- PDF resume upload
- Resume analysis
- ATS analysis
- AI resume review
- Job description matching
- Resume improvement
- Browser network requests
- Backend logs
- GitHub synchronization

---

# Engineering Design Decisions

## Modular Backend

The backend separates responsibilities into:

```text
API Routes
     |
     v
Schemas
     |
     v
Services
     |
     v
Utilities
```

This prevents the application from becoming dependent on a single large backend file.

---

## Dedicated Service Layer

Business logic is implemented inside dedicated service modules.

For example:

```text
api/ats.py
     |
     v
services/ats_service.py
```

The API layer handles HTTP requests while the service layer handles application-specific processing.

This improves:

- Maintainability
- Readability
- Testability
- Separation of concerns
- Future extensibility

---

## Environment-Based Configuration

Secrets and deployment-specific settings are stored outside the source code.

Examples include:

```text
GEMINI_API_KEY
GEMINI_MODEL
FRONTEND_URL
VITE_API_URL
PYTHON_VERSION
```

This allows the same codebase to support local development and production deployment.

---

## Separate Frontend and Backend Deployment

The frontend and backend are independently deployed:

```text
Vercel
 |
 +-- React + Vite Frontend

Render
 |
 +-- FastAPI Backend
```

This creates a clear separation between presentation and backend processing.

---

# Security Considerations

The project follows basic application security practices:

- API credentials are stored using environment variables.
- `.env` files are excluded from Git.
- Uploaded resume files are excluded from Git.
- Secrets are not hardcoded in frontend source code.
- Production CORS is configured for the known frontend origin.
- Deployment secrets are stored in platform environment variables.

---

# Limitations

## ATS Scoring

The ATS score is an analytical approximation based on the implemented analysis logic.

Different recruitment platforms use proprietary algorithms, so the score may differ from scores generated by commercial ATS systems.

---

## Generative AI

AI-generated recommendations may occasionally be incomplete, generalized, or context-dependent.

Users should review AI-generated recommendations before applying significant changes to a professional resume.

---

## PDF Extraction

The quality of extracted information depends on the structure and formatting of the uploaded PDF.

Image-only or highly complex PDF documents may produce less reliable extracted text.

---

## External AI Dependency

AI-powered functionality depends on the availability, latency, and response behavior of the Gemini API.

---

## Runtime Storage

The deployed backend uses an ephemeral runtime filesystem.

Uploaded resume files should therefore not be treated as permanent storage.

---

# Future Improvements

Potential future improvements include:

## Resume Intelligence

- Section-level resume scoring
- Advanced resume structure detection
- Better achievement and impact analysis
- Improved experience analysis
- Enhanced keyword extraction

## Job Matching

- Semantic job matching
- Embedding-based similarity
- Advanced skill ontology
- Role-specific matching
- Industry-specific keyword analysis

## AI Optimization

- Job-specific resume rewriting
- Multiple resume versions
- Personalized optimization strategies
- AI response quality evaluation
- Improved prompt evaluation

## User Platform

- User authentication
- Resume history
- Multiple resume profiles
- Persistent storage
- Resume version comparison
- Saved job descriptions

## Analytics

- Skill-gap visualization
- Resume performance analytics
- Job compatibility trends
- Resume improvement tracking

---

# Roadmap

## Version 1.0 - Current

```text
Production Application
       |
       +-- Resume Upload
       |
       +-- Resume Processing
       |
       +-- Resume Analysis
       |
       +-- ATS Analysis
       |
       +-- AI Resume Review
       |
       +-- Job Description Matching
       |
       +-- Resume Improvement
       |
       +-- Vercel Deployment
       |
       +-- Render Deployment
```

## Potential Future Direction

```text
Production v1.0
       |
       v
Advanced Resume Intelligence
       |
       v
Semantic Job Matching
       |
       v
Personalized Resume Optimization
       |
       v
Resume Intelligence Platform
```

---

# Technical Skills Demonstrated

This project demonstrates practical experience in:

### Artificial Intelligence

- Generative AI
- Google Gemini API
- AI-assisted text analysis
- AI-powered recommendations

### Natural Language Processing

- Text extraction
- Text cleaning
- Resume parsing
- Skill extraction
- Keyword analysis
- Job-description analysis

### Backend Engineering

- Python
- FastAPI
- REST API development
- Pydantic validation
- Service-oriented architecture
- API integration
- CORS configuration

### Frontend Engineering

- React
- Vite
- JavaScript
- Axios
- Component-based architecture
- API integration
- User interface development

### Document Processing

- PDF text extraction
- Resume parsing
- Structured resume information

### DevOps and Deployment

- Git
- GitHub
- Vercel
- Render
- Environment variables
- Production configuration
- Cloud deployment
- Production debugging

---

# Project Outcomes

This project demonstrates the complete lifecycle of a full-stack AI application:

```text
Problem Definition
       |
       v
System Design
       |
       v
Backend Development
       |
       v
AI Integration
       |
       v
Frontend Development
       |
       v
Testing
       |
       v
Git and GitHub
       |
       v
Cloud Deployment
       |
       v
Production Validation
```

The final application provides a public production interface where users can upload resumes and access resume analysis, ATS evaluation, AI-powered review, job-description matching, and resume improvement functionality.

---

# Screenshots

Screenshots of the application can be added to the repository in the future.

Recommended screenshots include:

1. Application homepage
2. Resume upload interface
3. ATS analysis results
4. AI resume review
5. Job match results
6. Resume improvement results

Example:

```markdown
![AI Resume Analyzer](path/to/screenshot.png)
```

Screenshots should only be referenced after the corresponding image files have been added to the repository.

---

# Author

## Vedansh

M.Tech Computer Science and Engineering

Areas of interest:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Generative AI
- AI Engineering
- Applied AI
- AI Research

GitHub:

https://github.com/Vedansh1011

---

# License

This project is intended for educational, research, and portfolio purposes.

---

# Project Summary

AI Resume Analyzer is a production-deployed full-stack AI application that combines PDF resume processing, ATS-oriented analysis, job-description matching, resume improvement, and Generative AI to provide actionable resume insights.

The project demonstrates the practical transition from local AI application development to a cloud-deployed production system.

The application integrates:

```text
React + Vite
      +
FastAPI
      +
PDF Processing
      +
Resume Analysis
      +
ATS Analysis
      +
Job Matching
      +
Google Gemini
      +
Vercel
      +
Render
```

### Live Application

https://ai-resume-analyzer-eight-lilac.vercel.app

### Backend API

https://ai-resume-analyzer-43et.onrender.com

### GitHub Repository

https://github.com/Vedansh1011/AI-Resume-Analyzer