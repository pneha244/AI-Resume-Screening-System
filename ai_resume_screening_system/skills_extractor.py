import re


SKILL_LIST = [
    "python",
    "java",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "machine learning",
    "deep learning",
    "data science",
    "artificial intelligence",
    "nlp",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",
    "streamlit",
    "flask",
    "django",
    "fastapi",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "git",
    "github",
    "excel",
    "power bi",
    "tableau",
    "statistics",
    "data analysis",
    "data visualization",
    "api"
]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9+#.\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def extract_skills(text):
    text = clean_text(text)

    found_skills = []

    for skill in SKILL_LIST:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def get_missing_skills(resume_skills, jd_skills):
    missing_skills = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    return sorted(missing_skills)