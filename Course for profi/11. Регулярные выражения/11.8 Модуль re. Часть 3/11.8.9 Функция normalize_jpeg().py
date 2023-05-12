import re


def normalize_jpeg(filename: str) -> str:
    return re.sub(r'\.(jpeg|jpg)$', r'.jpg', filename, flags=re.IGNORECASE)
