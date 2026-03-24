# 🔐 AI Secure Data Intelligence Platform
## 📌 Project Overview
AI Secure Data Intelligence Platform is a FastAPI-based backend application designed to analyze log files and detect sensitive information such as emails, passwords, and API keys. The system also evaluates risk levels and generates AI-based insights to improve security awareness.

---

## 🚀 Features
> 📂 Upload log files via API
> 🔍 Detect sensitive data:
  >> Emails
  >> Passwords
  >> API Keys
> ⚠️ Risk classification (Low / High / Critical)
> 🤖 AI-powered insights generation
> 📊 Structured JSON response
> 🌐 Interactive API testing using Swagger UI

---

## 🛠️ Tech Stack
> Python
> FastAPI
> Uvicorn

---

## 📂 Project Structure
ai_secure_platform/
│──> main.py          # FastAPI app (API endpoints)
│──> detector.py      # Logic for log analysis
│──> requirements.txt # Dependencies

---

## ⚙️ How to Run the Project

1. Install dependencies:
pip install -r requirements.txt

2. Run the server:
uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

---

## 📸 API Usage
> Open Swagger UI
> Use POST /analyze
> Upload a .txt log file
> Click Execute
> View results instantly

---

## 🎯 Example Output
{
  "summary": "Log analyzed",
  "findings": [
   {
      "type": "email",
      "risk": "low",
      "line": 2
    },
    {
      "type": "password",
      "risk": "critical",
      "line": 3
    },
    {
      "type": "api_key",
      "risk": "high",
      "line": 4
    }
  ],
  "risk_score": 3,
  "insights": [
    "Sensitive password exposed",
    "API key exposed in logs"
  ]
}

---

## 🎯 Use Cases
> Security log analysis
> Detecting sensitive data leaks
> AI-assisted risk monitoring
> Backend API development practice

---

## 👨‍💻 Author
Haridharani

---

## ⭐ Note
This project was developed as part of a hackathon to demonstrate backend development, API design, and basic AI-driven analysis.
