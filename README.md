# 🤖 AI Resume Analyzer and Job Recommendation System

## 📌 Project Overview

The AI Resume Analyzer and Job Recommendation System is an NLP-based application designed to help students understand how well their resume matches different job roles.

The system extracts information from PDF or DOCX resumes, identifies technical skills, compares the resume with job-role requirements, calculates match scores, recommends suitable job roles, identifies skill gaps, and generates a basic learning roadmap.

---

## 🎯 Project Objective

The main objective of this project is to help students:

- Analyze their resumes
- Identify technical and job-related skills
- Understand their suitability for different job roles
- Find missing skills
- Explore suitable career roles
- Follow a learning roadmap based on identified skill gaps

---

## ✨ Features

### 📄 Resume Upload
- Upload PDF resumes
- Upload DOCX resumes
- Extract resume text automatically

### 🧠 Skill Extraction
- Identify technical skills from resumes
- Use a controlled skill dictionary
- Group skills into relevant categories

### 📊 Resume Matching
- Compare resume content with job-role requirements
- Use TF-IDF vectorization
- Calculate cosine similarity
- Generate match scores

### 💼 Job Recommendations
The system analyzes multiple job roles and displays the top matching roles.

### ❌ Skill Gap Analysis
- Display skills already found
- Identify missing skills
- Compare skills against the selected target role

### 📚 Learning Roadmap
Generate a simple learning roadmap based on missing skills.

### 📥 Analysis Report
Download the generated resume analysis report as a text file.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | User interface |
| pypdf | PDF text extraction |
| python-docx | DOCX text extraction |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | TF-IDF and cosine similarity |
| Matplotlib | Visualization |

---

## 💼 Supported Job Roles

The initial dataset contains the following job roles:

1. Data Analyst
2. Machine Learning Engineer
3. AI Engineer
4. NLP Engineer
5. Computer Vision Engineer

---

## 📊 Matching Method

The project uses a beginner-friendly text matching approach.

### Step 1: Resume Text Extraction

The system extracts text from the uploaded PDF or DOCX resume.

### Step 2: Text Cleaning

The extracted text is normalized and cleaned before analysis.

### Step 3: Skill Extraction

The system searches the resume against the predefined skill dictionary.

### Step 4: TF-IDF

Resume content and job-role requirements are converted into TF-IDF vectors.

### Step 5: Cosine Similarity

Cosine similarity is used to calculate the similarity between the resume and each job role.

### Step 6: Role Recommendation

The job roles are ranked according to their calculated match scores.

---

## 🔍 Skill Gap Analysis

For the selected target role, the system compares:

**Resume Skills**

with

**Required Job Skills**

The result is divided into:

- ✅ Skills Found
- ❌ Missing Skills

The missing skills are then used to generate a learning roadmap.

---

## 📁 Project Structure

```text
ai_resume_analyzer/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── sample_resumes/
├── reports/
└── tests/
    └── test_cases.csv