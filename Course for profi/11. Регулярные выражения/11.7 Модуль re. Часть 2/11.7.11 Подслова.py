import re

data, word = input(), input()
print(len(re.findall(fr'\B{word}\B', data)))