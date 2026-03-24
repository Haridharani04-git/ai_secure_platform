from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from detector import analyze_log
import logging

app = FastAPI()

# ✅ Observability (logging)
logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    return {"message": "My project is running"}

@app.post("/analyze")
async def analyze(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    logging.info("Request received")

    # ✅ Multi-input handling
    if file:
        content = await file.read()
        text = content.decode("utf-8")

    elif text:
        pass

    else:
        return {"error": "No input provided"}

    # ✅ Security checks
    if not text.strip():
        return {"error": "Empty input"}

    if len(text) > 10000:
        return {"error": "Input too large"}

    # ✅ Analysis
    result = analyze_log(text)

    # ✅ BONUS: total issues count
    result["total_issues"] = len(result.get("findings", []))

    # ✅ Policy Engine
    if result["risk_score"] >= 3:
        result["action"] = "Block access immediately"
    elif result["risk_score"] == 2:
        result["action"] = "Review required"
    else:
        result["action"] = "Safe"

    logging.info("Analysis completed")

    return result