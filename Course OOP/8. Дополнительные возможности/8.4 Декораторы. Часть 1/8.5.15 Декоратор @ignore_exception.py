from functools import wraps, update_wrapper


class ignore_exception:
    def __init__(self, *args):
        self._expt_ = tuple(args)

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self._expt_ as err:
                print(f'Исключение {err.__class__.__name__} обработано')

        return wrapper
