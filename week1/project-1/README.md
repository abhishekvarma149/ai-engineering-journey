# 🤖 AI Resume Screening & Job Matching System

An AI-powered resume screening system that automatically analyzes resumes, extracts structured candidate information, and evaluates how well each candidate matches a given job description.

The project uses an LLM through the **Groq API** to perform resume parsing and candidate-job matching, while **Pydantic** is used to structure and validate the generated data.

---

## 🚀 Features

* 📄 Supports **PDF and DOCX resumes**
* 🤖 AI-powered resume parsing
* 🧠 Extracts skills, experience, education, projects, and certifications
* 💼 Automatically analyzes job descriptions
* 🎯 Matches candidates against job requirements
* 📊 Generates an overall match score from **0–100**
* ✅ Identifies matching skills
* ❌ Identifies missing important skills
* 💡 Generates an AI-based candidate verdict
* 📈 Sorts candidates by match score
* 🏆 Displays the top candidates
* ⚠️ Displays the lowest-matching candidates
* 🧩 Uses structured JSON output with Pydantic models

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │   Job Description   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Groq LLM        │
                    │   Job Description   │
                    │      Parsing        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Structured JobD   │
                    │     Pydantic        │
                    └──────────┬──────────┘
                               │
                               │
     ┌─────────────────────────┴─────────────────────────┐
     │                                                   │
     ▼                                                   ▼
┌───────────────┐                                ┌───────────────┐
│ PDF / DOCX    │                                │ JobD Object   │
│   Resumes     │                                │               │
└───────┬───────┘                                └───────┬───────┘
        │                                                │
        ▼                                                │
┌───────────────┐                                        │
│ Text          │                                        │
│ Extraction    │                                        │
└───────┬───────┘                                        │
        │                                                │
        ▼                                                │
┌───────────────┐                                        │
│   Groq LLM    │                                        │
│ Resume Parser │                                        │
└───────┬───────┘                                        │
        │                                                │
        ▼                                                │
┌───────────────┐                                        │
│   Resume      │                                        │
│   Pydantic    │                                        │
└───────┬───────┘                                        │
        │                                                │
        └────────────────────┬───────────────────────────┘
                             ▼
                    ┌─────────────────────┐
                    │   final_score()     │
                    │   LLM Comparison    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    MatchResult      │
                    │ Score + Details     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Sort Candidates     │
                    │ By Match Score      │
                    └──────────┬──────────┘
                               │
                      ┌────────┴────────┐
                      ▼                 ▼
                🏆 TOP 2           ⚠️ LOWEST 2
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                                |
| ----------------- | -------------------------------------- |
| **Python**        | Core programming language              |
| **Groq API**      | LLM inference                          |
| **GPT-OSS-120B**  | Language model used for analysis       |
| **Pydantic**      | Data validation and structured outputs |
| **pypdf**         | PDF text extraction                    |
| **python-docx**   | DOCX text extraction                   |
| **python-dotenv** | Environment variable management        |
| **pathlib**       | File and folder handling               |

---

## 📂 Project Structure

```text
day5/
│
├── resume_parser.py
├── .env
├── .gitignore
│
└── resumes/
    ├── candidate1.pdf
    ├── candidate2.pdf
    ├── candidate3.docx
    └── ...
```

### File responsibilities

**`resume_parser.py`**

Contains the complete application:

* Job description processing
* Pydantic schemas
* LLM prompts
* Resume parsing
* PDF/DOCX extraction
* Candidate scoring
* Candidate ranking

**`resumes/`**

Contains the candidate resumes that the application processes.

**`.env`**

Stores the Groq API key securely.

---

## 🔑 Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

⚠️ **Never commit your `.env` file to GitHub.**

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## 📦 Installation

Create and activate a virtual environment:

```bash
python -m venv day5
```

Activate it on macOS/Linux:

```bash
source day5/bin/activate
```

Install the required packages:

```bash
python -m pip install groq pydantic python-dotenv pypdf python-docx
```

---

## ▶️ Running the Project

Place your resumes inside:

```text
resumes/
```

Then run:

```bash
python resume_parser.py
```

The application will:

```text
1. Read the job description
        ↓
2. Extract structured job information
        ↓
3. Find resumes in the resumes folder
        ↓
4. Extract text from each resume
        ↓
5. Parse each resume using the LLM
        ↓
6. Compare the resume with the job
        ↓
7. Generate a match score
        ↓
8. Rank all candidates
        ↓
9. Display top and lowest candidates
```

---

## 🧠 How the AI Pipeline Works

### 1. Job Description Parsing

The job description is sent to the LLM.

The model extracts information such as:

```text
Role
Required Skills
Preferred Skills
Minimum Experience
Education Requirements
Responsibilities
```

The result is validated using the `JobD` Pydantic model. The project defines these structured job fields explicitly.

---

### 2. Resume Text Extraction

The application supports:

```text
PDF
DOCX
```

For PDF files, `pypdf` extracts text from each page.

For DOCX files, `python-docx` extracts text from paragraphs and tables.

---

### 3. Resume Parsing

The extracted resume text is sent to the LLM.

The model converts unstructured resume information into structured data:

```json
{
  "name": "Candidate Name",
  "email": "candidate@email.com",
  "phone": null,
  "total_experience_years": 1.5,
  "skills": [
    "Python",
    "C++",
    "AWS"
  ],
  "experiences": [],
  "education": [],
  "projects": [],
  "certifications": []
}
```

The project uses a `Resume` Pydantic model to define this structure.

---

### 4. Candidate Matching

The structured resume and structured job description are passed to the `final_score()` function.

The LLM evaluates:

* Matching skills
* Missing skills
* Experience requirement
* Overall match percentage
* Final candidate verdict

The result is stored in a `MatchResult` model containing a score and detailed evaluation.

---

### 5. Candidate Ranking

All candidates are stored in a list:

```python
all_results = []
```

Candidates are then sorted by their score:

```python
all_results.sort(
    key=lambda candidate: candidate["score"],
    reverse=True
)
```

The highest-scoring candidates are selected using:

```python
top_2 = all_results[:2]
```

and the lowest-scoring candidates using:

```python
worst_2 = all_results[-2:]
```

---

## 📊 Example Output

```text
============================================================
              TOP 2 CANDIDATES
============================================================

Candidate: Ashish Raj
Match Score: 78.0%

Matching Skills:
  ✓ Python
  ✓ C++
  ✓ Data Structures
  ✓ Algorithms
  ✓ AWS
  ✓ GitHub
  ✓ CI/CD
  ✓ Docker
  ✓ Kubernetes

Missing Important Skills:
  ✗ Database systems
  ✗ Open-source contributions
  ✗ OOP design experience

Experience Requirement:
  Relevant internship experience

Final Verdict:
Strong technical fit for required skills and many preferred
areas, but lacks database and open-source experience.

------------------------------------------------------------
```

---

## 💡 Key AI Engineering Concepts Learned

This project demonstrates several important AI engineering concepts:

### Structured LLM Output

Instead of accepting arbitrary text from the LLM:

```text
LLM → Text
```

the project uses:

```text
LLM
 ↓
JSON
 ↓
Pydantic
 ↓
Structured Python Object
```

### Prompt Engineering

The prompts instruct the model to:

* Follow a specific schema
* Return JSON
* Avoid inventing information
* Return `null` when information is unavailable
* Return empty lists when appropriate

### LLM-Based Information Extraction

The project converts:

```text
Unstructured Resume
        ↓
       LLM
        ↓
Structured Resume
```

### LLM-Based Decision Making

The project then performs:

```text
Job Description
       +
Candidate Resume
       ↓
      LLM
       ↓
Match Score + Analysis
```

---

## ⚠️ Current Limitations

This is a learning project and has some limitations:

* Match scores are generated by the LLM rather than a deterministic scoring formula.
* LLM responses can vary between runs.
* Resume formatting can affect text extraction.
* Scanned/image-only PDFs may not extract correctly.
* Only PDF and DOCX files are currently supported.
* There is no database or web interface yet.
* API calls include delays to reduce request frequency.

---

## 🔮 Future Improvements

Possible next versions could include:

* 🌐 Web interface using FastAPI + React
* 📊 Candidate dashboard
* 🗄️ PostgreSQL candidate database
* 🔍 Semantic skill matching using embeddings
* 📄 Support for scanned resumes using OCR
* 📧 Automated candidate email notifications
* 🔐 Authentication and recruiter accounts
* 📈 Candidate analytics dashboard
* ⚡ Async/batch processing
* 🧠 More deterministic scoring using weighted criteria
* ☁️ Deployment to AWS
* 🐳 Docker containerization
* 📑 Export candidate rankings to CSV/Excel

---

## 🎯 Project Goal

The goal of this project is to understand how LLMs can be integrated into a practical software application to process unstructured documents, extract structured information, and perform intelligent comparisons.

This project was built as part of my **AI Engineering learning journey**, focusing on:

```text
Python
   ↓
LLM APIs
   ↓
Prompt Engineering
   ↓
Structured Outputs
   ↓
Pydantic
   ↓
Document Processing
   ↓
AI Application
```

---

## 👨‍💻 Learning Outcome

By building this project, I learned how to:

* Work with the Groq API
* Send system and user messages to an LLM
* Generate structured JSON from LLM responses
* Use Pydantic models
* Create JSON schemas
* Parse PDF files
* Parse DOCX files
* Process multiple files using Python
* Build LLM-powered pipelines
* Compare structured data using an LLM
* Rank results using Python

---

## 📌 Disclaimer

This project is intended for **educational purposes** and should not be used as the sole decision-making system for real-world hiring.

AI-generated scores and evaluations should always be reviewed by a human recruiter.

---

## ⭐ Project Status

**Status:** Completed — Day 5 AI Engineering Learning Project

**Type:** AI / LLM Application

**Focus:** Resume Parsing + Job Matching + Candidate Ranking
