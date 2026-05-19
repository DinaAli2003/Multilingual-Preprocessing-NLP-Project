import re

def remove_punctuation(text: str):
    return re.sub(r"[^\w\s]", "", text)

def normalize_english(text: str):
    return text.lower()

def remove_extra_spaces(text: str):
    return " ".join(text.split())