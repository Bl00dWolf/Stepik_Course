import sys

data = {s.strip('\n').split(' - ')[0]: int(s.strip('\n').split(' - ')[1]) for s in sys.stdin.readlines()}

print(*filter(lambda name, num: num % 2 == 0, data))
