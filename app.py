import streamlit as st

from resume_analyzer import (
    extract_text_from_pdf,
    extract_skills,
    create_features,
    analyze_resume,
    match_job_roles
)

from ai_analyzer import generate_resume_feedback


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume using Machine Learning and Gemini AI "
    "to discover your skills, job-role matches, and improvement areas."
)

st.divider()


# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

st.subheader("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume in PDF format",
    type=["pdf"]
)


if uploaded_file is not None:

    # --------------------------------------------------
    # Save Uploaded Resume
    # --------------------------------------------------

    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())


    # --------------------------------------------------
    # Extract Resume Text
    # --------------------------------------------------

    resume_text = extract_text_from_pdf("uploaded_resume.pdf")


    # --------------------------------------------------
    # Detect Skills
    # --------------------------------------------------

    detected_skills = extract_skills(resume_text)

    detected = [
        skill
        for skill, value in detected_skills.items()
        if value == 1
    ]


    # --------------------------------------------------
    # ML Prediction
    # --------------------------------------------------

    resume_features = create_features(resume_text)

    result = analyze_resume(resume_features)


    # --------------------------------------------------
    # Job Role Matching
    # --------------------------------------------------

    job_matches = match_job_roles(detected_skills)

    top_roles = sorted(
        job_matches.items(),
        key=lambda x: x[1]["match_percentage"],
        reverse=True
    )


    # --------------------------------------------------
    # Resume Overview
    # --------------------------------------------------

    st.divider()

    st.subheader("📊 Resume Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Resume Match Level",
            result
        )

    with col2:
        st.metric(
            "Skills Detected",
            len(detected)
        )

    with col3:
        st.metric(
            "Job Roles Analyzed",
            len(job_matches)
        )


    # --------------------------------------------------
    # Detected Skills
    # --------------------------------------------------

    st.subheader("🛠️ Detected Skills")

    if detected:
        st.write(", ".join(detected))
    else:
        st.info("No skills were detected from the resume.")


    # --------------------------------------------------
    # Job Recommendations
    # --------------------------------------------------

    st.subheader("🏆 Top Job Recommendations")

    for i, (role, details) in enumerate(top_roles[:3], start=1):

        st.markdown(
            f"### {i}. {role}"
        )

        st.progress(
            details["match_percentage"] / 100
        )

        st.write(
            f"**Match:** {details['match_percentage']}%"
        )

        matched = ", ".join(details["matched_skills"])

        missing = ", ".join(details["missing_skills"])

        st.write(
            f"**Matched Skills:** {matched if matched else 'None'}"
        )

        st.write(
            f"**Skills to Learn:** {missing if missing else 'None'}"
        )

        st.divider()


    # --------------------------------------------------
    # Extracted Resume Text
    # --------------------------------------------------

    with st.expander("📄 View Extracted Resume Text"):

        st.text_area(
            "Resume content",
            resume_text,
            height=300
        )


    # --------------------------------------------------
    # Gemini AI Feedback
    # --------------------------------------------------

    st.subheader("🤖 AI Resume Feedback")

    with st.spinner("Gemini is analyzing your resume..."):

        feedback = generate_resume_feedback(
            resume_text,
            result,
            detected_skills,
            job_matches
        )

    st.write(feedback)