import itertools as it


def sum_of_digits(iterable):
    iterable = map(str, iterable)
    itt = it.chain.from_iterable(iterable)
    return sum(map(int, itt))


print(sum_of_digits([13, 20, 41, 2, 2, 5]))
