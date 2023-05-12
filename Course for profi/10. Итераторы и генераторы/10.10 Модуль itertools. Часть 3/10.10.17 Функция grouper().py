import itertools as it


# def grouper(iterable, n: int):
#     itt = iter(iterable)
#     return it.zip_longest(*(itt for _ in range(n)))


def grouper(iterable, n):
    return it.zip_longest(*[iter(iterable)] * n)
