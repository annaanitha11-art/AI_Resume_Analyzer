from ai_analyzer import generate_resume_feedback
from pypdf import PdfReader
import joblib
import pandas as pd
def extract_text_from_pdf(pdf_path):
    """
    Extract text from all pages of a PDF resume.
    """
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

# Load the trained model
model = joblib.load("model/model.pkl")


# Skills our system can recognize
skills = [
    "python",
    "java",
    "c",
    "sql",
    "machine learning",
    "web development",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "mongodb",
    "mysql",
    "data structures",
    "git",
    "apis",
    "spring boot",
    "pandas",
    "excel"
]

def extract_skills(resume_text):
    """
    Identify known skills from resume text.
    """

    resume_text = resume_text.lower()

    detected_skills = {}

    for skill in skills:
        if skill in resume_text:
            detected_skills[skill] = 1
        else:
            detected_skills[skill] = 0

    return detected_skills

def create_features(resume_text):
    """
    Convert resume text into the 8 features required by the ML model.
    """

    detected_skills = extract_skills(resume_text)

    features = {
        "python": detected_skills["python"],
        "java": detected_skills["java"],
        "sql": detected_skills["sql"],
        "machine_learning": detected_skills["machine learning"],
        "web_development": detected_skills["web development"],

        "projects": resume_text.lower().count("project"),
        "internship": 1 if "internship" in resume_text.lower() else 0,
        "experience": 1 if any(
    phrase in resume_text.lower()
    for phrase in [
        "work experience",
        "professional experience",
        "employment experience",
        "years of experience"
    ]
) else 0
    }

    return features

job_roles = {
    "Python Developer": [
        "python",
        "sql",
        "git",
        "apis"
    ],

    "Java Developer": [
        "java",
        "sql",
        "spring boot",
        "git"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "pandas",
        "excel"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "sql",
        "pandas"
    ]
}

def match_job_roles(detected_skills):
    """
    Compare detected resume skills with the required skills
    for each job role.
    """

    results = {}

    for role, required_skills in job_roles.items():

        matched_skills = []

        for skill in required_skills:
            if detected_skills.get(skill, 0) == 1:
                matched_skills.append(skill)

        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100

        results[role] = {
            "match_percentage": round(match_percentage, 2),
            "matched_skills": matched_skills,
            "missing_skills": [
                skill for skill in required_skills
                if skill not in matched_skills
            ]
        }

    return results
def analyze_resume(resume_features):
    """
    Predict the resume match level using the trained ML model.
    """

    features = pd.DataFrame([resume_features])

    prediction = model.predict(features)

    return prediction[0]


pdf_path = r"C:\Users\DELL\OneDrive\Documents\Anna_Anitha_Resume_Professional.pdf"

resume_text = extract_text_from_pdf(pdf_path)

print("\nExtracted Resume Text:")
print(resume_text)

detected_skills = extract_skills(resume_text)

print("\nDetected Skills:")
print(detected_skills)


features = create_features(resume_text)

print("\nML Features:")
print(features)

result = analyze_resume(features)

print("\nResume Match Level:", result)

job_matches = match_job_roles(detected_skills)

print("\nJob Role Matches:")

print("\n" + "=" * 40)
print("       TOP JOB RECOMMENDATIONS")
print("=" * 40)

sorted_jobs = sorted(
    job_matches.items(),
    key=lambda item: item[1]["match_percentage"],
    reverse=True
)

top_jobs = sorted_jobs[:3]

for index, (role, details) in enumerate(top_jobs, start=1):

    print(f"\n{index}. {role} — {details['match_percentage']}%")
    print("   Matched Skills:", ", ".join(details["matched_skills"]))
    print("   Missing Skills:", ", ".join(details["missing_skills"]))

feedback = generate_resume_feedback(
    resume_text,
    result,
    detected_skills,
    job_matches
)

print("\n" + "=" * 40)
print("         AI RESUME FEEDBACK")
print("=" * 40)
print(feedback)