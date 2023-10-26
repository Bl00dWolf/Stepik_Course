import functools


def auto_repr(args, kwargs):
    def wrapper(cls):
        old_repr = cls.__repr__

        @functools.wraps(old_repr)
        def new_repr(self):
            args_values = [repr(getattr(self, x)) for x in args]
            kwargs_dict = {k: v for k, v in zip(kwargs, [getattr(self, x) for x in kwargs])}
            kwargs_str = [f"{k}={repr(v)}" for (k, v) in kwargs_dict.items()]
            return f'{cls.__name__}({", ".join(map(str, args_values + kwargs_str))})'

        cls.__repr__ = new_repr
        return cls

    return wrapper

# норм решение:
# def auto_repr(args, kwargs):
#     def wrapper(cls):
#         def __repr__(self):
#             cls_args = [repr(self.__dict__[k]) for k in args]
#             cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
#             return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'
#
#         cls.__repr__ = __repr__
#         return cls
#
#     return wrapper
