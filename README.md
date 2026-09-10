# 📄 AI Resume Analyzer

An AI-powered resume analysis and job recommendation system built using **Python, Machine Learning, Streamlit, and Google Gemini AI**.

The application analyzes a resume in PDF format, extracts relevant skills, predicts an overall resume match level using a Machine Learning model, recommends suitable job roles, and provides personalized improvement suggestions using Gemini AI.

---

## 🚀 Features

* 📄 Upload a resume in PDF format
* 📝 Extract text from the uploaded resume
* 🛠️ Automatically detect technical skills
* 🤖 Predict resume match level using Machine Learning
* 🏆 Recommend suitable job roles
* 📊 Calculate skill-based job-role match percentages
* ❌ Identify missing skills for each recommended role
* ✨ Generate AI-powered resume feedback using Google Gemini
* 🌐 Interactive Streamlit web interface

---

## 🧠 How It Works

Resume PDF
     ↓
Extract Resume Text
     ↓
Detect Technical Skills
     ↓
Create ML Features
     ↓
Decision Tree Classifier
     ↓
Resume Match Level
     ↓
Job Role Matching
     ↓
Gemini AI Analysis
     ↓
Resume Feedback & Recommendations

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Analysis & Machine Learning

* Pandas
* Scikit-learn
* Decision Tree Classifier
* Joblib

### Resume Processing

* pypdf

### Generative AI

* Google Gemini API
* `google-genai`

### Web Application

* Streamlit

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

AI_Resume_Analyzer/
│
├── data/
│   └── resume_dataset.csv
│
├── model/
│   └── model.pkl
│
├── app.py
├── resume_analyzer.py
├── ai_analyzer.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/annaanitha11-art/AI_Resume_Analyzer.git

### 2. Open the project folder

cd AI_Resume_Analyzer

### 3. Install dependencies

python -m pip install -r requirements.txt

---

## 🔑 Gemini API Configuration

The application uses the Google Gemini API to generate resume feedback.

Create a Gemini API key and store it as an environment variable.

### Windows PowerShell

$env:GEMINI_API_KEY="YOUR_API_KEY"

Do **not** place your API key directly inside the Python source code or upload it to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application using:

python -m streamlit run app.py

The application will open in your browser.

Upload a PDF resume to begin the analysis.

---

## 📊 Example Analysis

For a sample Computer Science resume, the application can provide results such as:

Resume Match Level: Medium

Top Job Recommendations:

1. Web Developer — 75%
   Matched Skills: HTML, CSS, JavaScript
   Missing Skills: React

2. Python Developer — 25%
   Matched Skills: Python
   Missing Skills: SQL, Git, APIs

3. Java Developer — 25%
   Matched Skills: Java
   Missing Skills: SQL, Spring Boot, Git

The Gemini AI component then provides:

* Resume strengths
* Top recommended job role
* Matching skills
* Missing skills
* Resume improvement suggestions
* Recommended next steps

---

## 🤖 Machine Learning Model

The project uses a **Decision Tree Classifier** to predict the resume match level.

The model uses features such as:

* Python
* Java
* SQL
* Machine Learning
* Web Development
* Number of projects
* Internship experience
* Work experience

The model was trained using a small prototype dataset created for this project.

> **Note:** The current dataset is intentionally small and is suitable for demonstrating the project workflow. The resulting model performance should not be interpreted as real-world hiring accuracy.

---

## 💡 Job Recommendation System

The application compares detected resume skills against predefined skill requirements for different job roles.

Currently supported roles include:

* Python Developer
* Java Developer
* Web Developer
* Data Analyst
* Machine Learning Engineer

For each role, the system calculates a match percentage and identifies both matched and missing skills.

---

## ✨ Generative AI Component

Google Gemini is used as a career-assistance layer after the ML and rule-based analysis.

The application provides Gemini with:

* Extracted resume text
* ML match level
* Detected skills
* Job-role matching results

Gemini then generates concise, practical recommendations for improving the resume and preparing for suitable roles.

The AI is instructed to use only the information provided by the application and avoid inventing qualifications or experience.

---

## ⚠️ Limitations

* The current ML dataset is small and designed as a prototype.
* Skill detection currently relies on predefined technical skills.
* Job-role requirements are manually defined.
* The system does not replace professional recruitment or resume evaluation.
* AI-generated recommendations should be reviewed by the user before making career decisions.

---

## 🔮 Future Improvements

* Use a larger real-world resume/job dataset
* Improve NLP-based skill extraction
* Add more job roles
* Extract education and experience automatically
* Add resume section analysis
* Compare resumes directly with job descriptions
* Add ATS-style keyword analysis
* Deploy the application online
* Improve model evaluation using larger datasets

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python programming
* Data preprocessing
* Machine Learning
* Classification
* PDF text extraction
* Rule-based skill matching
* Generative AI integration
* Streamlit application development
* Git and GitHub
* Building an end-to-end AI/ML application

---

## 👩‍💻 Author

**Anna Anitha**

B.Tech Computer Science & Engineering
JNTUH College of Engineering Sultanpur

---

## 📌 Project Repository

GitHub: https://github.com/annaanitha11-art/AI_Resume_Analyzer