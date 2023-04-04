# мое решение фигня
# def pairwise(iterable):
#     itt = list(iterable)
#     it = iter(itt)
#     next(it, None)
#     for elem in itt:
#         yield elem, next(it, None)

def pairwise(iterable):
    it = iter(iterable)
    i = next(it, None)
    while i is not None:
        i, prev = next(it, None), i
        yield prev, i


# numbers = [1, 2, 3, 4, 5]
# print(*pairwise(numbers))

# iterator = iter('stepik')
# print(*pairwise(iterator))