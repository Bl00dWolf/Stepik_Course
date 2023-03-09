from functools import wraps


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result
        else:
            raise TypeError
    return wrapper
