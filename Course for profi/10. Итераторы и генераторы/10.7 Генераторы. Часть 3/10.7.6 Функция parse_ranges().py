def parse_ranges(string: str):
    diap = (st for st in string.split(','))
    diap2 = (range(int(ab.split('-')[0]), int(ab.split('-')[1]) + 1) for ab in diap)
    for ran in diap2:
        yield from ran

# еще вариант
# def parse_ranges(ranges: str):
#     for r in ranges.split(","):
#         start, end = map(int, r.split("-"))
#         yield from range(start, end+1)

# print(*parse_ranges('1-2,4-4,8-10'))
