def prefix(string: str, to_the_end: bool = False):
    def decor(func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            else:
                return string + func(*args, **kwargs)

        return wrapper

    return decor
