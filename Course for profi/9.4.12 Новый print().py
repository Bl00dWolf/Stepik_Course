old_print = print


def print(*args, sep=' ', end='\n'):
    old_print(*map(lambda x: x.upper() if isinstance(x, str) else x, args), sep=sep.upper(), end=end.upper())


print('beegeek', [1, 2, 3], 4)