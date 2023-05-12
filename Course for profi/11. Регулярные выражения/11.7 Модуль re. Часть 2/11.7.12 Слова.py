import re

data, word = input(), input()
print(len(re.findall(fr'\b{word}\b', data)))
