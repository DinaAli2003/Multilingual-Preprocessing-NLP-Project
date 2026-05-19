import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from src.config.stopwords import english_stopwords
from src.utils.cleaners import remove_punctuation, normalize_english, remove_extra_spaces

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

stop_words = set(stopwords.words("english"))
known_stopwords = stop_words.union(english_stopwords)
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def process_english(text, config):
    if not text:
        return ""

    if config.normalize:
        text = normalize_english(text)

    if config.remove_punctuation:
        text = remove_punctuation(text)

    tokens = [token for token in nltk.word_tokenize(text) if token.strip()]

    if config.remove_stopwords:
        tokens = [token for token in tokens if token.lower() not in known_stopwords or len(token) > 3]

    if config.stemming:
        tokens = [stemmer.stem(token) for token in tokens]

    if config.lemmatize:
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return remove_extra_spaces(" ".join(tokens))
