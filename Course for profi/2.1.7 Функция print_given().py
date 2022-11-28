def print_given(*args, **kwargs):
    [print(arg, type(arg)) for arg in args]
    [print(k, v, type(v)) for k, v in sorted(kwargs.items())]


print_given(b=2, d=4, c=3, a=1)
