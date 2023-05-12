import re

word, data = input()[:-2], input()
print(len(re.findall(fr'\b{word}[zs]e\b', data, re.I)))