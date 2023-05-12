import csv

n = int(input()) - 1

with open('deniro.csv', encoding='UTF-8') as file:
    rows = list(csv.reader(file))
    if rows[0][n].isdigit():
        for row in sorted(rows, key=lambda x: int(x[n])):
            print(','.join(row))
    else:
        for row in sorted(rows, key=lambda x: x[n]):
            print(','.join(row))

# Более компактный вариант
# import csv
#
# i = int(input()) - 1
#
# with open('deniro.csv', 'r', encoding='utf-8') as file:
#     data = list(csv.reader(file))
#
# data.sort(key=lambda x: int(x[i]) if x[i].isdigit() else x[i])
# for lst in data:
#     print(*lst, sep=',')