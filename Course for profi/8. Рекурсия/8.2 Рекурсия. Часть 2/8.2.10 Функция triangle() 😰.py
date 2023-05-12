def triangle(h: int) -> None:
    if h > 0:
        triangle(h - 1)
        print('*' * h)