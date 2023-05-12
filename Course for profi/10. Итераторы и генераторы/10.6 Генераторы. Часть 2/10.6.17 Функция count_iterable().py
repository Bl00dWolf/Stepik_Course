def count_iterable(iterable):
    return sum(1 for _ in iter(iterable))


print(count_iterable(range(1, 10000000000000)))
