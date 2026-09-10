import os
from google import genai


def generate_resume_feedback(resume_text, match_level, detected_skills, job_matches):
    """
    Use Gemini AI to analyze the resume using the results
    produced by our ML model and job-matching system.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "GEMINI_API_KEY environment variable is not set."

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a helpful career advisor analyzing a Computer Science student's resume.

Use ONLY the information provided below. Do not invent skills,
experience, achievements, or qualifications.

Resume:
{resume_text}

ML Resume Match Level:
{match_level}

Detected Skills:
{detected_skills}

Job Role Matching Results:
{job_matches}

Provide concise and practical feedback with these sections:

1. Resume Strengths
2. Top Recommended Job Role
3. Skills That Match the Role
4. Missing Skills to Learn
5. Resume Improvement Suggestions
6. Recommended Next Steps

Focus on actionable advice suitable for a Computer Science student.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text

