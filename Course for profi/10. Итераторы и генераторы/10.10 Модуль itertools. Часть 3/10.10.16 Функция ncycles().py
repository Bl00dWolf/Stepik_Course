import itertools as it


def ncycles(iterable, times: int):
    for i in it.tee(iterable, times):
        yield from i


print(*ncycles([1, 2, 3, 4], 3))
