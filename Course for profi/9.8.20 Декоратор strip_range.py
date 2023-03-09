from functools import wraps


def strip_range(start: int, end: int, char: str = '.'):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result[:start] + char * len(result[start:end]) + result[end:]

        return wrapper

    return decor
