import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def calculate_match_score(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    jd_words = set(job_description.split())
    resume_words = set(resume_text.split())

    if len(jd_words) == 0:
        return 0

    matched_words = jd_words.intersection(resume_words)

    score = (len(matched_words) / len(jd_words)) * 100

    return round(score, 2)


def get_matched_keywords(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    jd_words = set(job_description.split())
    resume_words = set(resume_text.split())

    matched_keywords = jd_words.intersection(resume_words)

    return ", ".join(sorted(matched_keywords))