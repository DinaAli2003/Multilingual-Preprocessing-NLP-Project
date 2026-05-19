from fastapi import FastAPI
from src.routers import preprocess

app = FastAPI(
    title="Multilingual Text Preprocessor",
    description="FastAPI backend for English and Arabic text preprocessing.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Multilingual Text Preprocessor API", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(preprocess.router)
