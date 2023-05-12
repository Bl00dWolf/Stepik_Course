class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if not len(string) >= 9:
        raise LengthError
    elif string == string.lower() or string == string.upper():
        raise LetterError
    elif not any(i.isdigit() for i in string):
        raise DigitError
    return True


while True:
    try:
        if is_good_password(input()):
            print('Success!')
            break
    except PasswordError as er:
        print(er.__class__.__name__)
