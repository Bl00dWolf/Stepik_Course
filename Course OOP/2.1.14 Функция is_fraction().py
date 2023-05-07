import re


def is_fraction(string: str) -> bool:
    if re.fullmatch(r'-?\d+/([1-9]\d*|0+\d+)', string):
        return True
    return False