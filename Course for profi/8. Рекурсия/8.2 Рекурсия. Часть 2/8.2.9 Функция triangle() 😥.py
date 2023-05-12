def triangle(h: int) -> None:
    if h > 0:
        print('*' * h)
        triangle(h - 1)
