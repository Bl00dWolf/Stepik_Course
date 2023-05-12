import sys

data = [int(d) for d in sys.stdin.readlines()]

if data:
    print('нет учеников')
else:
    print(f'Рост самого низкого ученика: {min(data)}\nРост самого высокого ученика: {max(data)}')
    print(f'Средний рост: {sum(data) / len(data)}')
