# 🤖 Candidate Portfolio AI

An AI-powered candidate portfolio that allows recruiters, interviewers, and visitors to interact with a candidate through a conversational AI assistant.

Instead of simply displaying a static resume, the system converts the candidate's resume into structured information and uses an LLM to answer questions about the candidate's **skills, experience, education, projects, and certifications**.

The AI is grounded in the candidate's actual portfolio data and is instructed not to invent information.

---

## ✨ What is Candidate Portfolio AI?

Traditional portfolios provide recruiters with static information such as:

* Resume
* Skills
* Projects
* Education
* Experience
* Certifications

**Candidate Portfolio AI** makes this information interactive.

A visitor can ask:

> "What technologies does the candidate know?"

> "Tell me about their projects."

> "What experience do they have with FastAPI?"

> "What is their educational background?"

The AI analyzes the candidate's portfolio data and provides a conversational response.

---

## 🚀 Features

### 📄 AI Resume Parser

Extracts meaningful information from the candidate's PDF resume and converts it into structured data.

Extracted information includes:

* Name
* Email
* Phone
* Total experience
* Skills
* Work experience
* Internships
* Education
* Projects
* Certifications

### 🧠 Structured Candidate Profile

The extracted information is validated using **Pydantic models**, creating a structured candidate profile that can be used by the AI.

### 💬 AI Portfolio Assistant

Visitors can ask questions about the candidate through a conversational interface.

For example:

```text
What are the candidate's technical skills?
```

```text
Tell me about their projects.
```

```text
What technologies have they worked with?
```

### 🛡️ Grounded Responses

The AI is instructed to use only information available in the candidate's portfolio.

It should not invent:

* Skills
* Companies
* Projects
* Experience
* Education
* Achievements

When information is unavailable, the assistant responds:

```text
I don't have enough information to answer that.
```

### ⚡ FastAPI Backend

The project provides a lightweight backend API for processing the candidate's portfolio and handling AI conversations.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │  Candidate Resume   │
                    │        PDF          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    PDF Extraction   │
                    │       pypdf         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Resume Text      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Groq LLM       │
                    │   Resume Parser     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Structured Resume  │
                    │   Pydantic Model    │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────────┐
                 │   Candidate Portfolio Data  │
                 └──────────────┬──────────────┘
                                │
                    Visitor asks a question
                                │
                                ▼
                    ┌─────────────────────┐
                    │      AI Assistant   │
                    │      Groq LLM       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Grounded Response  │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| **Python**        | Backend development       |
| **FastAPI**       | REST API                  |
| **Groq**          | LLM inference             |
| **Qwen**          | Language model            |
| **Pydantic**      | Structured candidate data |
| **pypdf**         | PDF text extraction       |
| **python-dotenv** | Environment configuration |
| **Uvicorn**       | Development server        |

---

## 📁 Project Structure

```text
candidate-portfolio-ai/
│
├── main.py
├── my_resume.pdf
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## 🔄 How It Works

### 1. Resume as the Candidate's Source of Information

The candidate's resume acts as the initial source of portfolio information.

```text
my_resume.pdf
```

### 2. Extract Resume Content

`pypdf` extracts the text from the PDF.

```text
PDF
 ↓
pypdf
 ↓
Resume Text
```

### 3. Convert Resume Into Structured Data

The resume text is passed to the LLM with a predefined schema.

The model extracts information such as:

```json
{
  "name": "Candidate Name",
  "skills": [
    "Python",
    "FastAPI",
    "React"
  ],
  "projects": [
    "AI Portfolio",
    "Resume Parser"
  ],
  "education": [
    "B.Tech Computer Science"
  ]
}
```

The output is then validated using Pydantic.

### 4. Build the AI Candidate Profile

The structured resume becomes the knowledge available to the portfolio assistant.

```text
Resume
   ↓
Structured Candidate Profile
   ↓
AI Portfolio Assistant
```

### 5. Answer Visitor Questions

When a visitor asks a question, the candidate profile is provided to the LLM as context.

The AI then generates a response based on the available candidate information.

---

## 💬 Example Interaction

### Visitor

```text
What technologies does the candidate work with?
```

### Candidate Portfolio AI

```text
The candidate has experience with technologies including
Python, FastAPI, React, and other tools mentioned in their
portfolio.
```

---

### Visitor

```text
Does the candidate have experience with Django?
```

### Candidate Portfolio AI

```text
I don't have enough information to answer that.
```

This prevents the AI from presenting unsupported information as a candidate skill.

---

## 🔌 API

### `GET /`

Loads and parses the candidate's resume.

#### Response

```json
{
  "message": "Resume parsed!"
}
```

---

### `POST /chat`

Allows visitors to interact with the candidate's AI assistant.

#### Request

```json
{
  "question": "What are the candidate's skills?"
}
```

#### Response

```json
{
  "answer": "The candidate has experience with Python, FastAPI, React..."
}
```

---

## 📚 API Documentation

Once the server is running, FastAPI provides interactive documentation at:

```text
http://127.0.0.1:8000/docs
```

The API can be tested directly through Swagger UI.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd candidate-portfolio-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn groq pydantic pypdf python-dotenv
```

### 4. Configure the API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

### 5. Add the candidate resume

Place the resume in the project directory:

```text
my_resume.pdf
```

### 6. Run the application

```bash
uvicorn main:app --reload
```

Or with `uv`:

```bash
uv run uvicorn main:app --reload
```

---

## 🧠 AI Design

The project uses two LLM workflows.

### Resume Understanding

The first workflow converts unstructured resume content into structured candidate information.

```text
Unstructured Resume
        ↓
    LLM Parsing
        ↓
Structured JSON
        ↓
Pydantic Validation
```

### Candidate Assistant

The second workflow uses the structured candidate profile as context.

```text
Visitor Question
       ↓
Candidate Profile
       ↓
    LLM
       ↓
Grounded Response
```

The assistant is explicitly instructed to:

1. Use only candidate information.
2. Never invent information.
3. Return an appropriate response when information is unavailable.
4. Respond professionally.
5. Represent the candidate during interactions.

---

## 🎯 Use Cases

Candidate Portfolio AI can be used for:

* 👨‍💻 Developer portfolios
* 🎓 Student portfolios
* 💼 Job applications
* 🧑‍💼 Recruiter interactions
* 🏆 Project showcases
* 📋 Resume-based Q&A
* 🌐 Interactive personal websites

Instead of recruiters manually searching through a long resume, they can directly ask questions about the candidate.

---

## 🔮 Future Improvements

The current version focuses on the backend AI workflow.

Planned improvements include:

* [ ] Interactive portfolio frontend
* [ ] Resume upload
* [ ] Website content ingestion
* [ ] Project-specific knowledge
* [ ] GitHub profile integration
* [ ] LinkedIn information integration
* [ ] Semantic search / RAG
* [ ] Vector database
* [ ] Conversation history
* [ ] Streaming responses
* [ ] Multiple candidate profiles
* [ ] Authentication
* [ ] Docker deployment
* [ ] Cloud deployment
* [ ] Voice-based candidate interaction

---

## 📌 Current Status

### Completed

* [x] PDF resume extraction
* [x] AI-powered resume parsing
* [x] Structured candidate schema
* [x] Pydantic validation
* [x] Candidate AI assistant
* [x] Grounded AI responses
* [x] FastAPI backend
* [x] Groq LLM integration
* [x] Environment variable configuration

### Planned

* [ ] Portfolio website
* [ ] Website content ingestion
* [ ] RAG
* [ ] Vector database
* [ ] GitHub integration
* [ ] Streaming chat
* [ ] Deployment

---

## 🎓 What I Learned

Through this project, I explored practical AI engineering concepts including:

* LLM API integration
* Prompt engineering
* Structured LLM output
* JSON schemas
* Pydantic models
* Document processing
* Context-based prompting
* Grounded generation
* Hallucination control
* FastAPI
* REST APIs
* Environment variables

---

## 👨‍💻 Author

**Abhishek Verma**

B.Tech — Computer Science Engineering

Interested in **AI Engineering, Generative AI, Backend Development, and AI-powered applications**.

---

## ⭐ Project Overview

**Candidate Portfolio AI** transforms a traditional static portfolio into an interactive AI-powered experience.

```text
Resume + Portfolio Data
          ↓
     AI Processing
          ↓
Structured Candidate Profile
          ↓
   Conversational AI
          ↓
     Recruiter / Visitor
```

The goal is to make candidate portfolios **interactive, searchable, and conversational** rather than simply presenting static information.
