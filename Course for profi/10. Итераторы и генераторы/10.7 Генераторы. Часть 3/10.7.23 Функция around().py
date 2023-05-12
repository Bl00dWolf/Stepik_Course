def around(iterable):
    it = iter(iterable)
    nx = next(it, None)
    prev = None
    while nx is not None:
        nx, cur = next(it, None), nx
        yield prev, cur, nx
        prev = cur


iterator = iter('hey')
print(*around(iterator))

numbers = [1, 2, 3, 4, 5]
print(*around(numbers))