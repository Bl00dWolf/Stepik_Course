def intersperse(iterable, delimiter):
    itt = iter(iterable)
    cur = next(itt, (None, None, 0x1F))
    while cur != (None, None, 0x1F):
        yield cur
        cur = next(itt, (None, None, 0x1F))
        if cur != (None, None, 0x1F):
            yield delimiter
    else:
        return


# еще вариант:
# def intersperse(iterable, delimiter):
#     first = True
#     for item in iterable:
#         if not first:
#             yield delimiter
#         first = False
#         yield item