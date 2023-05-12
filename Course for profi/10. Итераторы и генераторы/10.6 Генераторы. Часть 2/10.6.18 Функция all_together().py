def all_together(*args):
    for iterr in args:
        yield from (elem for elem in iterr)

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))