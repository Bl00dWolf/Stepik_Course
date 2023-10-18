from functools import wraps


class type_check:
    def __init__(self, types: list | tuple):
        self.types = types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for tp, arg in zip(self.types, args):
                if not isinstance(arg, tp):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper
