from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()

class Request(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "AI Summarizer Agent is running!"}

@app.post("/summarize")
def summarize(req: Request):
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception("Missing API key")

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Summarize this text in 3-4 lines:\n{req.text}"
        )

        return {"summary": response.text}

    except Exception:
        text = req.text
        short = text[:150] + "..." if len(text) > 150 else text

        return {
            "summary": f"(Fallback) {short}",
            "note": "Fallback used"
        }
