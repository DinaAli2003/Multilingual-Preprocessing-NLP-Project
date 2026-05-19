import re

def is_arabic(text):
    return re.search(r'[\u0600-\u06FF]', text)

def is_english(text):
    return re.search(r'[a-zA-Z]', text)