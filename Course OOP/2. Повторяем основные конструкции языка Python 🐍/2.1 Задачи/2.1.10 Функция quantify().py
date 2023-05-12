def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return len(list(filter(lambda x: predicate(x), iterable)))

# еще вариант:
# def quantify(iterable, predicate):
#     if predicate is None:
#         predicate = bool
#     return sum(map(predicate, iterable))
