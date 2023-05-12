from itertools import accumulate


def factorials(n: int):
    return accumulate(range(1, n + 1), lambda x, y: x * y)


# numbers = factorials(6)
# print(*numbers)
