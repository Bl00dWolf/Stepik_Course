from functools import wraps


def returns(datatype):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, datatype):
                return res
            else:
                raise TypeError

        return wrapper

    return decor
