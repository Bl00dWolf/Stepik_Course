def with_previous(iterable):
    prev = None
    for i in iterable:
        yield i, prev
        prev = i


# numbers = [1, 2, 3, 4, 5]
# print(*with_previous(numbers))
#
# Интересное решение с моржовым оператором
# def with_previous(iterable):
#     prev = None
#     return ((i, prev, prev := i)[:-1] for i in iterable)
