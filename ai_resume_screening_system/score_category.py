def get_score_category(score):
    if score >= 75:
        return "Excellent Match"

    elif score >= 50:
        return "Good Match"

    elif score >= 30:
        return "Average Match"

    else:
        return "Low Match"


def get_selection_status(score, missing_skills):
    if score >= 75 and len(missing_skills) <= 2:
        return "Shortlisted"

    elif score >= 50:
        return "Review Required"

    else:
        return "Rejected"