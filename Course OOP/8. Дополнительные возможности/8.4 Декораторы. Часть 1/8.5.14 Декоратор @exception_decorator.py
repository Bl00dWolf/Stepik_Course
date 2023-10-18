from functools import wraps, update_wrapper


class exception_decorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs), None
        except Exception as err:
            return None, err.__class__
