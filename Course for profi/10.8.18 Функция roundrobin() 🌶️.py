from itertools import cycle, count, accumulate


def roundrobin(*args):
    itts = []
    for arg in args:
        itts.append(iter(arg))

    if not itts:
        return

    n = 1
    while n is not None:
        for i in range(len(itts)):
            n = next(itts[i], None)
            if n is not None:
                yield n


# numbers = [1, 2, 3]
# letters = iter('beegeek')
#
# print(*roundrobin(numbers, letters))

# print(list(roundrobin()))

# TEST_4:
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = range(5)
letters = iter('beegeek')

print(*roundrobin(numbers1, letters))

# TEST_4:
# 1 0 b 2 1 e 3 2 e 4 3 g 5 4 e 6 e 7 k 8 9 10