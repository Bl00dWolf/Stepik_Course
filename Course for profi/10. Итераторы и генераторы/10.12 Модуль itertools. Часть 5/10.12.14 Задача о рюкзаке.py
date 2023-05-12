from collections import namedtuple
import itertools as it

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

mass_limit = int(input())
good_load = {}

for size in range(1, len(items) + 1):
    combs = it.combinations(items, r=size)
    for combination in set(combs):
        cur_mass = sum(item.mass for item in combination)
        if cur_mass <= mass_limit:
            total_price = sum(item.price for item in combination)
            good_load[total_price] = list(combination)

if good_load:
    items = good_load[max(good_load)]
    for item in sorted(items):
        print(item.name)
else:
    print('Рюкзак собрать не удастся')