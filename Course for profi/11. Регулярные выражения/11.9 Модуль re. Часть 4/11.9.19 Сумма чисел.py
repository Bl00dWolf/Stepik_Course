import re

start, end = [int(i) for i in input().split()]
res = re.compile(r'\d+').findall(input(), pos=start, endpos=end)
print(sum(map(int, res)))