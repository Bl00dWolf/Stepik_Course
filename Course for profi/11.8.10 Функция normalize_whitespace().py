import re


def normalize_whitespace(string: str) -> str:
    return re.sub(r'\s{2,}', r' ', string)


print(normalize_whitespace('AAAA                A                AAAA'))
