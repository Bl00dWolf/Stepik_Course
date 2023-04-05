import itertools as it


def first_largest(iterable, number):
    try:
        index, num = next(it.dropwhile(lambda x: x[1] < number, enumerate(iterable)))
        return index
    except StopIteration:
        return -1


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))
