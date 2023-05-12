from collections import Counter
import json
import csv

lof_dicts_sales = []
for fname in ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']:
    with open(fname, encoding='UTF-8') as file:
        lof_dicts_sales.extend(list(csv.DictReader(file)))

with open('prices.json', encoding='UTF-8') as file2:
    prices = json.load(file2)

money = Counter()
for ddict in lof_dicts_sales:
    tovar, m1_sales, m2_sales, m3_sales = ddict.values()
    money[tovar] += prices[tovar] * (int(m1_sales) + int(m2_sales) + int(m3_sales))
print(money.total())

