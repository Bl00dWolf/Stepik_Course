from functools import wraps


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not isinstance(res, self.datatype):
                raise TypeError
            return res

        return wrapper
