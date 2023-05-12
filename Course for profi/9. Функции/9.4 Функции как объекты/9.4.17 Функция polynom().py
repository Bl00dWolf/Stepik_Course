def polynom(x: int):
    polynom.__dict__.setdefault('values', set())
    val = x ** 2 + 1
    if val not in polynom.values:
        polynom.values.add(val)
    return val


