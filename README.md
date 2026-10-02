# AI Resume Screening System

A Streamlit-powered web application that automates resume screening by extracting candidate details, parsing skills, matching resumes against a job description, and calculating a candidate match score.

## Project Overview

The AI Resume Screening System is an intelligent web-based application developed using Python and Streamlit that automates screening and shortlisting resumes based on a provided job description.

Recruiters often review hundreds of resumes manually, which is time-consuming, inefficient, and error-prone. This project solves that problem by automatically extracting resume content, identifying important skills, comparing resumes with job requirements, and ranking candidates based on their match score.

The system supports uploading multiple resumes in PDF and DOCX formats and provides a modern interactive dashboard for efficient hiring decisions.

## Objectives

- Automate the resume screening process
- Reduce manual HR effort
- Improve hiring efficiency
- Identify best matching candidates automatically
- Extract candidate details from resumes
- Analyze technical skills and missing skills
- Generate resume ranking and shortlisting output

## Features

### Core Features
- Multiple resume uploads
- PDF resume support
- DOCX resume support
- Job description input
- Resume text extraction
- Keyword matching
- Match percentage calculation
- Skill extraction
- Missing skill detection
- Resume ranking
- Candidate shortlisting

### Advanced Features
- Candidate name extraction
- Email extraction
- Phone number extraction
- Score categorization
- Smart selection status
- Dashboard analytics
- Resume preview
- CSV report download
- Interactive Streamlit UI
- Candidate filtering system

## Technologies Used

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python      | Backend logic             |
| Streamlit   | Web application framework |
| Pandas      | Data processing           |
| PyPDF2      | PDF text extraction       |
| python-docx | DOCX file reading         |
| Regex       | Email & phone extraction  |

## System Architecture

```text
User uploads resume files
            ↓
Resume parser extracts text
            ↓
Skill extraction module
            ↓
Job description comparison
            ↓
Match score calculation
            ↓
Candidate ranking
            ↓
Dashboard & result generation
```

## Modules

### Resume Parser Module

Extracts text content from uploaded PDF and DOCX resumes.

Functions:
- PDF reading
- DOCX reading
- Resume text extraction

### Skill Extraction Module

Identifies technical skills present in resumes and job descriptions.

Examples:
- Python
- SQL
- Machine Learning
- Streamlit
- Django

### Matching Engine Module

Compares resume content with the job description and calculates matching percentage.

Outputs:
- Match score
- Matched keywords
- Missing skills

### Candidate Information Module

Extracts:
- Candidate name
- Email address
- Phone number

using regular expressions and text processing.

### Dashboard Module

Displays:
- Total resumes
- Shortlisted candidates
- Rejected candidates
- Best matching resume
- Candidate table

## How it Works

1. User uploads multiple resumes.
2. User enters the job description.
3. System extracts resume text.
4. Skills are identified from resumes.
5. Resumes are compared with the job description.
6. Match score is calculated.
7. Candidates are categorized.
8. Dashboard displays results.
9. Recruiter downloads CSV report.

## Advantages

- Saves recruitment time
- Reduces manual screening effort
- Improves hiring accuracy
- Handles multiple resumes together
- Easy-to-use interface
- Fast candidate filtering

## Requirements

- Python 3.8+

## Installation

1. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Run the app

```powershell
cd "AI_Resume_Screening_System"
python -m streamlit run app.py
```

Then open the displayed local URL in your browser (typically `http://localhost:8501`).

## Files

- `app.py` - Streamlit application entry point
- `candidate_info.py` - Extracts email, phone, and candidate name
- `matcher.py` - Computes resume-job match score and matched keywords
- `skills_extractor.py` - Extracts skills and missing skills from resumes and job descriptions
- `resume_parser.py` - Reads and parses resume text from PDF and DOCX files
- `score_category.py` - Converts numeric scores into categories and shortlist status
- `requirements.txt` - Python dependencies

## Notes

- Supports PDF and DOCX resumes
- Built for quick screening and shortlist recommendations
