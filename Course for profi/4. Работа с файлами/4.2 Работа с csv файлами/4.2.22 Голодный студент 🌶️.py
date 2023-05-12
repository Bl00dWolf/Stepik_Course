import csv

with open('prices.csv', encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)

tovars = {}
for dictt in data:
    # создаем словарь, где ключ это название магазина, а значение это тюпл - название самого дешевого товара и его цена
    tovars[dictt['Магазин']] = min(dictt.items(), key=lambda x: int(x[1]) if x[1].isdigit() else 999999)
# магазин с самым дешевым товаром, сортируем по цене, если она одинаковая, то по имени товара, если имя одинаковое,
# то по названию магазина
cheepest = min(tovars, key=lambda x: (int(tovars.get(x)[1]), tovars.get(x)[0], x))
print(f'{tovars[cheepest][0]}: {cheepest}')

# Еще решение
# import csv
#
# with open('prices.csv', encoding='UTF-8') as f:
#     h, *rows = csv.reader(f, delimiter=';')
#
# goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
# cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
#
# print(f'{cheapest[1]}: {cheapest[0]}')