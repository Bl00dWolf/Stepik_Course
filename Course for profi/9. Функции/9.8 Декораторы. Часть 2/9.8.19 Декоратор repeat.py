def repeat(times: int):
    def decor(func):
        from functools import wraps

        @wraps(func)
        def wrapper(*args, **kwargs):
            [func(*args, **kwargs) for _ in range(times - 1)]
            return func(*args, **kwargs)

        return wrapper

    return decor
