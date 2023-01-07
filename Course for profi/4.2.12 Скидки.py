import csv

with open('sales.csv', encoding='UTF-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
        if int(row['old_price']) - int(row['new_price']) > 0:
            print(row['name'])