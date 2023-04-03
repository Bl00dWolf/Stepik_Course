def pairwise(iterable):
    it = iter(iterable)
    while True:
        v1 = next(it, None)
        v2 = next(it, None)
        if v1 and v2:
            yield v1, v2
        else:
            break


numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))
