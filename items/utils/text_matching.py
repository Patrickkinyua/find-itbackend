import re
from rapidfuzz import fuzz

def normalize_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def text_similarity(a, b):
    a = normalize_text(a)
    b = normalize_text(b)

    score1 = fuzz.token_set_ratio(a, b)
    score2 = fuzz.token_sort_ratio(a, b)
    score3 = fuzz.partial_ratio(a, b)

    return (score1 * 0.4 + score2 * 0.4 + score3 * 0.2)
