import sys

data = [int(s) for s in sys.stdin.readlines()]

if data[-1] % 2 == 0 and len(data) % 2 == 0 or data[-1] % 2 == 1 and len(data) % 2 == 1:
    print('Дима')
else:
    print('Анри')

# еще решение
# import sys
# s = tuple(int(i.strip()) for i in sys.stdin.readlines())
# print(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])
