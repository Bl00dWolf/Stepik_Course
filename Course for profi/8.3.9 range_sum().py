def range_sum(numbers: list[int], start: int, end: int) -> int:
    if start == end:
        return numbers[end]
    else:
        return 0 + range_sum(numbers[start:], start, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
