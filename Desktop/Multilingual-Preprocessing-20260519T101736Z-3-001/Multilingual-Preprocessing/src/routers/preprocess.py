from fastapi import APIRouter, HTTPException
from src.models.schema import PreprocessRequest, PreprocessResponse
from src.services.english_services import process_english
from src.services.arabic_services import process_arabic
from src.utils.validators import is_arabic, is_english

router = APIRouter()

@router.post("/process", response_model=PreprocessResponse)
def preprocess_text(req: PreprocessRequest):
    language = req.language.strip().lower()

    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Empty text")

    if language not in {"en", "ar"}:
        raise HTTPException(status_code=400, detail="Language must be 'en' or 'ar'")

    if language == "en" and not is_english(req.text):
        raise HTTPException(status_code=400, detail="Text not English")

    if language == "ar" and not is_arabic(req.text):
        raise HTTPException(status_code=400, detail="Text not Arabic")

    if language == "en":
        result = process_english(req.text, req)
    else:
        result = process_arabic(req.text, req)

    return PreprocessResponse(original=req.text, processed=result)
