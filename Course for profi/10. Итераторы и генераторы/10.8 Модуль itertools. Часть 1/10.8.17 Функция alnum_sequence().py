from itertools import cycle, count
from string import ascii_uppercase


def alnum_sequence():
    letters = cycle(ascii_uppercase)
    nums = cycle(range(1, len(ascii_uppercase) + 1))
    while True:
        num, letter = next(nums), next(letters)
        yield num
        yield letter

# еще вариант:

# def alnum_sequence():
#     for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
#         yield from item

# alnum = alnum_sequence()
# print(*(next(alnum) for _ in range(55)))
#
# alnum = alnum_sequence()
# print(*(next(alnum) for _ in range(100)))