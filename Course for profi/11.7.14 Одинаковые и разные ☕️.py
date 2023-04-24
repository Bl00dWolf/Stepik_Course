import re

word, data = input()[:-3], input()
print(len(re.findall(fr'\b{word}ou?r\b', data, re.I)))