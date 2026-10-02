import re


def extract_email(text):
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_pattern, text)

    if emails:
        return emails[0]

    return "Not Found"


def extract_phone(text):
    phone_pattern = r"(\+91[\s-]?)?[6-9]\d{9}"
    phones = re.findall(phone_pattern, text)

    match = re.search(phone_pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_candidate_name(text):
    lines = text.strip().split("\n")

    for line in lines:
        line = line.strip()

        if line and len(line.split()) <= 4:
            if not any(char.isdigit() for char in line):
                return line.title()

    return "Not Found"