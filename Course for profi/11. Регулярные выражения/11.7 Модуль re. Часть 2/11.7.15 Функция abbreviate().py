import re


def abbreviate(phrase: str) -> str:
    found = re.findall(r'\b\w|\B[A-Z]', phrase)
    return ''.join(found).upper()
