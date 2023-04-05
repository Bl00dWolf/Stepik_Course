import itertools as it


def drop_this(iterable, obj):
    return it.dropwhile(lambda x: x == obj, iterable)

iterator = iter('bbbbeebee')
print(*drop_this(iterator, 'b'))