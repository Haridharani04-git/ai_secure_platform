from fastapi import FastAPI, UploadFile, File
from detector import analyze_log

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My project is running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    result = analyze_log(text)

    return result