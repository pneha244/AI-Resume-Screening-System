# AI-Powered Resume Screening System

## Project Synopsis

### Project Title

AI-Powered Resume Screening System

---

# 1. Introduction

The AI-Powered Resume Screening System is an intelligent web-based application developed using Python and Streamlit that automates the process of screening and shortlisting resumes based on a given job description.

In traditional recruitment systems, HR teams manually review hundreds of resumes, which is time-consuming, inefficient, and prone to human error. This project solves that problem by automatically extracting resume content, identifying important skills, comparing resumes with job requirements, and ranking candidates according to their matching score.

The system supports multiple resume uploads in PDF and DOCX formats and provides a modern interactive dashboard for recruiters.

---

# 2. Objective of the Project

The main objectives of this project are:

• Automate resume screening process
• Reduce manual HR effort
• Improve hiring efficiency
• Identify best matching candidates automatically
• Extract candidate details from resumes
• Analyze technical skills and missing skills
• Generate resume ranking and shortlisting reports

---

# 3. Features of the System

## Core Features

• Multiple Resume Upload
• PDF Resume Support
• DOCX Resume Support
• Job Description Input
• Resume Text Extraction
• Keyword Matching
• Match Percentage Calculation
• Skill Extraction
• Missing Skill Detection
• Resume Ranking
• Candidate Shortlisting

---

## Advanced Features

• Candidate Name Extraction
• Email Extraction
• Phone Number Extraction
• Score Categorization
• Smart Selection Status
• Dashboard Analytics
• Resume Preview
• CSV Report Download
• Interactive Streamlit UI
• Candidate Filtering System

---

# 4. Technologies Used

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python      | Backend Logic             |
| Streamlit   | Web Application Framework |
| Pandas      | Data Processing           |
| PyPDF2      | PDF Text Extraction       |
| python-docx | DOCX File Reading         |
| Regex       | Email & Phone Extraction  |

---

# 5. System Architecture

```text
User Uploads Resume Files
            ↓
Resume Parser Extracts Text
            ↓
Skill Extraction Module
            ↓
Job Description Comparison
            ↓
Match Score Calculation
            ↓
Candidate Ranking
            ↓
Dashboard & Result Generation
```

---

# 6. Modules of the Project

## 6.1 Resume Parser Module

This module extracts text content from uploaded PDF and DOCX resumes.

Functions:
• PDF Reading
• DOCX Reading
• Resume Text Extraction

---

## 6.2 Skill Extraction Module

This module identifies technical skills present in resumes and job descriptions.

Examples:
• Python
• SQL
• Machine Learning
• Streamlit
• Django

---

## 6.3 Matching Engine Module

This module compares resume content with the job description and calculates matching percentage.

Outputs:
• Match Score
• Matched Keywords
• Missing Skills

---

## 6.4 Candidate Information Module

This module extracts:

• Candidate Name
• Email Address
• Phone Number

using regular expressions and text processing.

---

## 6.5 Dashboard Module

Displays:

• Total Resumes
• Shortlisted Candidates
• Rejected Candidates
• Best Matching Resume
• Candidate Table

---

# 7. Working of the System

Step 1:
User uploads multiple resumes.

Step 2:
User enters job description.

Step 3:
System extracts resume text.

Step 4:
Skills are identified from resumes.

Step 5:
Resumes are compared with job description.

Step 6:
Match score is calculated.

Step 7:
Candidates are categorized.

Step 8:
Dashboard displays results.

Step 9:
Recruiter downloads CSV report.

---

# 8. Advantages of the System

• Saves recruitment time
• Reduces manual screening effort
• Improves hiring accuracy
• Handles multiple resumes together
• Easy to use interface
• Fast candidate filtering
• Better recruitment analytics

---

# 9. Limitations

• Basic NLP implementation
• Skill matching depends on predefined keywords
• Resume formatting may affect extraction quality
• No database integration in current version

---

# 10. Future Enhancements

• AI-based semantic matching
• OpenAI/Gemini integration
• Interview recommendation system
• Resume scoring using Machine Learning
• ATS compatibility checking
• Database integration
• Email automation for recruiters
• Candidate analytics dashboard
• Authentication system
• Cloud deployment

---

# 11. Folder Structure

```text
AI_Resume_Screening_System/
│
├── app.py
├── resume_parser.py
├── matcher.py
├── skills_extractor.py
├── candidate_info.py
├── score_category.py
├── requirements.txt
```

---

# 12. Installation Steps

## Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

## Step 2: Create Project Folder

```bash
mkdir AI_Resume_Screening_System
cd AI_Resume_Screening_System
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 4: Install Required Libraries

Create `requirements.txt`

```txt
streamlit
pandas
PyPDF2
python-docx
```

Install libraries:

```bash
pip install -r requirements.txt
```

---

# 13. How to Run the Project

## Step 1

Open terminal inside project folder.

---

## Step 2

Run Streamlit application:

```bash
streamlit run app.py
```

---

## Step 3

Browser will open automatically.

Default URL:

```text
http://localhost:8501
```

---

# 14. Input and Output

## Input

• Multiple Resume Files
• Job Description

---

## Output

• Match Percentage
• Candidate Ranking
• Shortlisted Candidates
• Missing Skills
• Dashboard Analytics
• CSV Report

---

# 15. Sample Job Description

```text
We are looking for a Python Developer with knowledge of SQL, Machine Learning, Streamlit, Django, Pandas, and API development.
```

---

# 16. Sample Output

| Candidate    | Match Score | Status          |
| ------------ | ----------- | --------------- |
| Rahul Sharma | 88%         | Shortlisted     |
| Aman Kumar   | 72%         | Review Required |
| Riya Singh   | 35%         | Rejected        |

---

# 17. Conclusion

The AI-Powered Resume Screening System is an efficient recruitment automation solution that simplifies resume analysis and candidate shortlisting. The project demonstrates the practical use of Python, Streamlit, text processing, and skill extraction techniques in real-world HR technology systems.

This system can significantly reduce hiring effort and improve recruiter productivity while providing a scalable foundation for future AI-powered recruitment solutions.

---

# 18. Developed By

Name: Dhiraj Kr
Profession: GenAI Developer & Data Scientist

💫 End of Document 💫
