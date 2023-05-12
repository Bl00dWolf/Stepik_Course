from copy import deepcopy


def get_min_max(iterable) -> tuple:
    iter2 = deepcopy(iterable)
    try:
        return min(iter(iterable)), max(iter(iter2))
    except:
        return None


# еще вариант
# def get_min_max(iterable):
#     iterable = iter(iterable)
#     try:
#         smallest = largest = next(iterable)
#     except:
#         return None
#     for elem in iterable:
#         if elem < smallest:
#             smallest = elem
#         if elem > largest:
#             largest = elem
#     return smallest, largest