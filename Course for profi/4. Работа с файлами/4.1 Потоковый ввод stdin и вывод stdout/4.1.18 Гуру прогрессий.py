import sys

data = [int(d.strip()) for d in sys.stdin.readlines()]

arif = [data[0]]
[arif.append(arif[i] + (data[1] - data[0])) for i in range(len(data) - 1)]

geom = [data[0]]
[geom.append(geom[i] * (data[1] / data[0])) for i in range(len(data) - 1)]

if data == arif:
    print('Арифметическая прогрессия')
elif data == geom:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
