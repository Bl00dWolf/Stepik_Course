old_print = print


def upper(func):
    def wrapper(*args, **kwargs):
        n_args = []
        n_kwargs = {}
        for arg in args:
            n_args.append(str(arg).upper())
        for k, v in kwargs.items():
            n_kwargs[k] = str(v).upper()
        return func(*n_args, **n_kwargs)
    return wrapper


@upper
def print(*args, **kwargs):
    return old_print(*args, **kwargs)


# еще вариант
# def new_print(func):
#     def wrapper(*args, sep=' ', end='\n'):
#         func(sep.join(map(str, args)).upper(), end = end.upper())
#     return wrapper
#
# print = new_print(print)
