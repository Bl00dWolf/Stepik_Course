def is_good_password(string: str) -> bool:
    if len(string) >= 9 and any(i.isdigit() for i in string) and string != string.lower() and string != string.upper():
        return True
    return False


# print(is_good_password('Passrtghtr'))
