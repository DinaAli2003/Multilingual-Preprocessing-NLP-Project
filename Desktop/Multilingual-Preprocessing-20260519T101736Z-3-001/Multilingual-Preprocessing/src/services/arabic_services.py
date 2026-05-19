import re
from pyarabic.araby import strip_tashkeel, strip_tatweel
from src.config.stopwords import arabic_stopwords
from src.utils.cleaners import remove_punctuation


def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ي", text)
    text = re.sub("[ءٱ]", "ا", text)
    return text


def process_arabic(text, config):
    if not text:
        return ""

    if config.normalize:
        text = normalize_arabic(text)
        text = strip_tashkeel(text)
        text = strip_tatweel(text)

    if config.remove_punctuation:
        text = remove_punctuation(text)

    words = [word for word in text.split() if word.strip()]

    if config.remove_stopwords:
        words = [word for word in words if word not in arabic_stopwords or len(word) > 3]

    return " ".join(words)
