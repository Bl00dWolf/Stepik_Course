from itertools import cycle, count, accumulate

# не совсем верный вариант зато мой
def roundrobin(*args):
    itts = []
    for arg in args:
        itts.append(iter(arg))

    if not itts:
        return

    is_over_id = [True for _ in range(len(itts))]
    while any(is_over_id):
        for i in range(len(itts)):
            n = next(itts[i], '<seq_end>')
            if n != '<seq_end>':
                yield n
            else:
                is_over_id[i] = False

# еще вариант
# def roundrobin(*args):
#     iters = tuple(iter(a) for a in args)
#     while True:
#         err_counter = 0
#         for i in iters:
#             try: res = next(i)
#             except: err_counter += 1
#             else: yield res
#         if err_counter == len(iters):
#             break


# numbers = [1, 2, 3]
# letters = iter('beegeek')
#
# print(*roundrobin(numbers, letters))

# print(list(roundrobin()))

# TEST_4:
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 = range(5)
# letters = iter('beegeek')
#
# print(*roundrobin(numbers1, letters))

# 1 0 b 2 1 e 3 2 e 4 3 g 5 4 e 6 e 7 k 8 9 10

# TEST_9:
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))

# 1 None 2 None 3 None None
