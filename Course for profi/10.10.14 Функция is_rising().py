import itertools as it


def is_rising(iterable):
    for el in it.pairwise(iterable):
        if not el[0] < el[1]:
            return False
    return True

# еще вариант
# def is_rising(iterable):
#     return all(a < b for a, b in pairwise(iterable))
