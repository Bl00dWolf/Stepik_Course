import sys

summ, other_count = 0.0, 0
for line in sys.stdin.readlines():
    try:
        summ += float(line)
    except ValueError:
        other_count += 1

if summ.is_integer():
    summ = int(summ)
print(f'{summ}\n{other_count}')
