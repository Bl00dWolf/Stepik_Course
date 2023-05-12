import re

data = input()


def rewind(string: re.Match) -> str:
    return string.group(2) * int(string.group(1))


while re.search(r'(\d+)\((\w+)\)', data):
    data = re.sub(r'(\d+)\((\w+)\)', rewind, data)
print(data)

# еще вариант
# from re import subn
#
# s, n = input(), 1
#
# while n:
#     s, n = subn(r'(\d+)\((\w*)\)', lambda m: m[2] * int(m[1]), s)
#
# print(s)