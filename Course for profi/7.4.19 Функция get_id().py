def get_id(names: list, name: str) -> int:
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    elif not (name.isalpha() and name[0].isupper() and name[1:].islower()):
        raise ValueError('Имя не является корректным')
    return len(names) + 1
