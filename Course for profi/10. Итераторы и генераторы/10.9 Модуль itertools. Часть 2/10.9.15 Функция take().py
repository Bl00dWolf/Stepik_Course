import itertools as it


def take(iterable, n: int):
    return it.islice(iterable, n)


print(*take(range(10), 5))
