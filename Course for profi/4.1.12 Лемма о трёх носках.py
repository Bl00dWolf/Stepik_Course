import sys

data = [int(s) for s in sys.stdin.readlines()]

if data[-1] % 2 == 0 and len(data) % 2 == 0:
    print('Анри')
else:
    print('Дима')
