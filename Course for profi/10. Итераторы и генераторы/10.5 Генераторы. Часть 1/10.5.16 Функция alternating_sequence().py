def alternating_sequence(count: int = None):
    num = 1
    if count is None:
        count = -1
    while count:
        count -= 1
        if num % 2 == 0:
            yield -num
        else:
            yield num
        num += 1


gen = alternating_sequence(10)
print(*gen)