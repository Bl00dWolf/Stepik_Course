from functools import wraps, update_wrapper


class takes_numbers:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args_cond = len(list(filter(lambda x: not isinstance(x, int | float), args))) != 0
        kwarg_cond = len(list(filter(lambda x: not isinstance(x, int | float), kwargs.values()))) != 0
        if args_cond or kwarg_cond:
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
