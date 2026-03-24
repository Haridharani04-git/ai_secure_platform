from fastapi import FastAPI, UploadFile, File, Form
from detector import analyze_log
app = FastAPI()
@app.post("/analyze")
async def analyze(file: UploadFile = File(None), text: str = Form(None)):
    if file:
        content = await file.read()
        text_data = content.decode("utf-8")
    elif text:
        text_data = text
    else:
        return {"error": "No input provided"}
    return analyze_log(text_data)