import streamlit as st
import pandas as pd

from resume_parser import extract_resume_text
from matcher import calculate_match_score, get_matched_keywords
from skills_extractor import extract_skills, get_missing_skills
from candidate_info import extract_email, extract_phone, extract_candidate_name
from score_category import get_score_category, get_selection_status


st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


# -------------------------------
# CUSTOM CSS
# -------------------------------

st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #1e293b;
    text-align: center;
    margin-bottom: 5px;
}

.sub-title {
    font-size: 18px;
    color: #64748b;
    text-align: center;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
}

.section-heading {
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    margin-top: 20px;
    margin-bottom: 12px;
}

.success-box {
    padding: 18px;
    border-radius: 14px;
    background: #dcfce7;
    color: #166534;
    font-weight: 600;
    border-left: 6px solid #22c55e;
}

.best-box {
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
    border: 1px solid #c7d2fe;
    color: #1e293b;
    font-size: 17px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# HEADER
# -------------------------------

st.markdown(
    "<div class='main-title'>AI-Powered Resume Screening System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Upload multiple resumes, compare with job description, extract skills, and shortlist candidates automatically.</div>",
    unsafe_allow_html=True
)

st.divider()


# -------------------------------
# SIDEBAR
# -------------------------------

with st.sidebar:
    st.header("Screening Settings")

    min_score = st.slider(
        "Minimum Shortlisting Score",
        min_value=0,
        max_value=100,
        value=60
    )

    show_resume_text = st.checkbox(
        "Show Extracted Resume Preview",
        value=False
    )

    st.info(
        "Recommended Score:\n\n"
        "75+ Excellent\n\n"
        "50+ Good\n\n"
        "30+ Average\n\n"
        "Below 30 Low"
    )


# -------------------------------
# INPUT SECTION
# -------------------------------

left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("<div class='section-heading'>Upload Resumes</div>", unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "Upload PDF or DOCX resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} resume(s) uploaded successfully.")

with right_col:
    st.markdown("<div class='section-heading'>Job Description</div>", unsafe_allow_html=True)

    job_description = st.text_area(
        "Paste Job Description",
        height=230,
        placeholder="Example: We need a Python Developer with SQL, Django, Machine Learning, Pandas, Streamlit..."
    )


st.divider()


# -------------------------------
# SCREENING LOGIC
# -------------------------------

if st.button("Start Resume Screening", use_container_width=True):

    if not uploaded_files:
        st.warning("Please upload at least one resume.")

    elif not job_description.strip():
        st.warning("Please enter job description.")

    else:
        results = []

        jd_skills = extract_skills(job_description)

        for file in uploaded_files:
            resume_text = extract_resume_text(file)

            match_score = calculate_match_score(
                resume_text,
                job_description
            )

            matched_keywords = get_matched_keywords(
                resume_text,
                job_description
            )

            resume_skills = extract_skills(resume_text)

            missing_skills = get_missing_skills(
                resume_skills,
                jd_skills
            )

            score_category = get_score_category(match_score)

            selection_status = get_selection_status(
                match_score,
                missing_skills
            )

            if match_score < min_score:
                selection_status = "Rejected"

            results.append({
                "Candidate Name": extract_candidate_name(resume_text),
                "Email": extract_email(resume_text),
                "Phone": extract_phone(resume_text),
                "File Name": file.name,
                "Match Score (%)": match_score,
                "Score Category": score_category,
                "Selection Status": selection_status,
                "Resume Skills": ", ".join(resume_skills),
                "Required Skills": ", ".join(jd_skills),
                "Missing Skills": ", ".join(missing_skills),
                "Matched Keywords": matched_keywords,
                "Resume Preview": resume_text[:700]
            })

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Match Score (%)",
            ascending=False
        )

        shortlisted_count = len(df[df["Selection Status"] == "Shortlisted"])
        review_count = len(df[df["Selection Status"] == "Review Required"])
        rejected_count = len(df[df["Selection Status"] == "Rejected"])

        st.markdown(
            "<div class='success-box'>Resume screening completed successfully.</div>",
            unsafe_allow_html=True
        )

        st.divider()


        # -------------------------------
        # DASHBOARD
        # -------------------------------

        st.markdown("<div class='section-heading'>Screening Dashboard</div>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Resumes", len(uploaded_files))
        col2.metric("Shortlisted", shortlisted_count)
        col3.metric("Review Required", review_count)
        col4.metric("Rejected", rejected_count)


        st.divider()


        # -------------------------------
        # BEST CANDIDATE
        # -------------------------------

        best_candidate = df.iloc[0]

        st.markdown("<div class='section-heading'>Best Matching Candidate</div>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class='best-box'>
                Candidate: {best_candidate['Candidate Name']}<br>
                File: {best_candidate['File Name']}<br>
                Match Score: {best_candidate['Match Score (%)']}%<br>
                Status: {best_candidate['Selection Status']}<br>
                Email: {best_candidate['Email']}<br>
                Phone: {best_candidate['Phone']}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.divider()


        # -------------------------------
        # FILTER RESULT
        # -------------------------------

        st.markdown("<div class='section-heading'>Filter Candidates</div>", unsafe_allow_html=True)

        status_filter = st.selectbox(
            "Filter by Selection Status",
            ["All", "Shortlisted", "Review Required", "Rejected"]
        )

        if status_filter != "All":
            filtered_df = df[df["Selection Status"] == status_filter]
        else:
            filtered_df = df


        # -------------------------------
        # RESULT TABLE
        # -------------------------------

        st.markdown("<div class='section-heading'>Screening Result</div>", unsafe_allow_html=True)

        display_columns = [
            "Candidate Name",
            "Email",
            "Phone",
            "File Name",
            "Match Score (%)",
            "Score Category",
            "Selection Status",
            "Resume Skills",
            "Missing Skills"
        ]

        st.dataframe(
            filtered_df[display_columns],
            use_container_width=True,
            height=420
        )


        # -------------------------------
        # RESUME PREVIEW
        # -------------------------------

        if show_resume_text:
            st.markdown("<div class='section-heading'>Resume Text Preview</div>", unsafe_allow_html=True)

            for index, row in filtered_df.iterrows():
                with st.expander(row["File Name"]):
                    st.write(row["Resume Preview"])


        # -------------------------------
        # DOWNLOAD CSV
        # -------------------------------

        csv_data = df.drop(columns=["Resume Preview"]).to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Screening Result CSV",
            data=csv_data,
            file_name="resume_screening_result.csv",
            mime="text/csv",
            use_container_width=True
        )