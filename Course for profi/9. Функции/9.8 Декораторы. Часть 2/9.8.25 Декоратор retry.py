from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal times
            while times != 0:
                try:
                    return func(*args, **kwargs)
                except:
                    times -= 1
                    continue
            raise MaxRetriesException

        return wrapper

    return decor
