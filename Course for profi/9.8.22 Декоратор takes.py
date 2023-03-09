from functools import wraps


def takes(*typess):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not all(map(lambda x: isinstance(x, typess), args)) or not all(
                    map(lambda x: isinstance(x, typess), kwargs.values())):
                raise TypeError
            return res

        return wrapper

    return decor

# @takes(list)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
#
#
# print(append_this.__name__)
# print(append_this.__doc__)
#
# try:
#     print(append_this([1, 2], 3))
# except TypeError as e:
#     print(type(e))
