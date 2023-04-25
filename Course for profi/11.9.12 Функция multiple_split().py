import re


def multiple_split(string: str, delimiters: list[str]) -> list[str]:
    return re.split(r'|'.join(map(re.escape, delimiters)), string)
