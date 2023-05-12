def recursive_sum(a: int, b: int) -> int:
    if a == 0:
        return b
    else:
        return 1 + recursive_sum(a - 1, b)


print(recursive_sum(10, 22))
