from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}')
        return func(*args, **kwargs)
    return wrapper

# @trace
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
# print(beegeek())
# print(beegeek.__name__)
# print(beegeek.__doc__)