def get_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return a * get_pow(a, n - 1)
