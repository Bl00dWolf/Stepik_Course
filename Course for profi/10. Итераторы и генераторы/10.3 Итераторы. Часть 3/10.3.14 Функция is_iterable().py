# def is_iterable(obj):
#     return '__iter__' in dir(obj)

is_iterable = lambda obj: '__iter__' in dir(obj)