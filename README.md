# 🤖 AI Summarizer Agent (Gemini + FastAPI + Cloud Run)

Live Demo: https://ai-agent-721769240731.asia-south1.run.app

## 📌 Overview
This project is a simple AI agent that summarizes input text using Google's Gemini API.  
It is built using FastAPI and deployed on Google Cloud Run.

---

## 🚀 Features
- Accepts input text via HTTP POST request
- Returns a concise 3–4 line summary
- Uses Gemini API for AI-based summarization
- Includes fallback logic if API fails
- Fully deployed and accessible via public URL

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Google Gemini API (`google-genai`)
- Docker
- Google Cloud Run

---

## 📡 API Endpoints

### 1. Health Check
**GET /**

Returns:
{
"message": "AI Summarizer Agent is running!"
}


"message": "AI Summarizer Agent is running!"

---
### 2. Summarize Text
**POST /summarize**

Request:
```json
{
  "text": "Your input text here"
}
```
Response:
{
  "summary": "Summarized Text"
}


Live Deployement:
Base url:
https://ai-agent-721769240731.asia-south1.run.app/

Swagger docs:
https://ai-agent-721769240731.asia-south1.run.app/docs

Setup Instructions (Local)
Clone repo:
git clone https://github.com/your-username/ai-agent.git
cd ai-agent

Install dependencies:
pip install -r requirements.txt

Set API Key:
export GEMINI_API_KEY=your_api_key_here

Run server:
uvicorn main:app --reload

                                                                                                                                                                    
Install dependencies:
pip install -r  requirements.txt

Set API Key:



uvicorn main:app --reload

Deployment:
Deployed using Google Cloud Run with Docker Container.

Note:
If Gemini API quota is exceeded, the app returns a fallback summary to ensure reliability.

Author:
Aisha Sultana

#2. `.gitignore`
Create:

```bash
nano.gitignore

Paste:
__pycache__/
*.pyc
.env
venv/

