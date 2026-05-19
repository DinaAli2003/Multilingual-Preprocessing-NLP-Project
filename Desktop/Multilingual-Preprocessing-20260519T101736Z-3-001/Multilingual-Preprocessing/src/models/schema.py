from pydantic import BaseModel

class PreprocessRequest(BaseModel):
    text: str
    language: str  # "en" or "ar"
    remove_stopwords: bool = True
    lemmatize: bool = False
    stemming: bool = False
    remove_punctuation: bool = True
    normalize: bool = True


class PreprocessResponse(BaseModel):
    original: str
    processed: str