from functools import wraps


def add_attrs(**dicks):
    def decor(func):
        for k, v in dicks.items():
            func.__dict__[k] = v

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decor


# @add_attrs(attr1='bee', attr2='geek')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)

# еще вариант
# import functools
#
# def add_attrs(**attrs):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         wrapper.__dict__ |= attrs
#         return wrapper
#     return decorator