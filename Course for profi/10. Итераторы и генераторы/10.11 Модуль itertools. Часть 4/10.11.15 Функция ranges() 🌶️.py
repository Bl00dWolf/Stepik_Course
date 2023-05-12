from itertools import groupby


def ranges(numbers: list[int]) -> list[tuple]:
    ranges = []
    gp = groupby(numbers, key=lambda x: x - numbers.index(x))
    for k, v in gp:
        tempo = list(v)
        ranges.append((min(tempo), max(tempo)))
    return ranges


numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))
