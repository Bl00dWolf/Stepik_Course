def starmap(func, iterable):
    print(*zip(*iterable))
    return map(func, *zip(*iterable))


# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
#
# print(*starmap(lambda x, y, z: x * y * z, points))
