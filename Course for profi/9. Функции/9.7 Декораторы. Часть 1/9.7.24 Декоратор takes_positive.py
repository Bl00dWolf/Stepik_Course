def takes_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            elif arg <= 0:
                raise ValueError
        for _, v in kwargs.items():
            if not isinstance(v, int):
                raise TypeError
            elif v <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
# except Exception as err:
#     print(type(err))