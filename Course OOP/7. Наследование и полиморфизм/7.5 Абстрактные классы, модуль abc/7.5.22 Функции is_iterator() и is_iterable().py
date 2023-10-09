def is_iterable(obj):
    return hasattr(obj, '__iter__')


def is_iterator(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__')

# еще вариант
# from collections.abc import Iterator, Iterable
#
#
# def is_iterable(obj):
#     return isinstance(obj, Iterable)
#
#
# def is_iterator(obj):
#     return isinstance(obj, Iterator)