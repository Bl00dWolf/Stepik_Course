def unique(iterable):
    ddict = {}
    for elem in iterable:
        ddict[elem] = ddict.setdefault(elem, 0) + 1
    yield from iter(ddict)


# еще решение

# def unique(iterable):
#     yield from {i: 0 for i in iterable}


numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))
