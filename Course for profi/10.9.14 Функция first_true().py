import itertools as it


def first_true(iterable, predicate):
    return next(filter(predicate, iterable), None)


# TEST_4:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))