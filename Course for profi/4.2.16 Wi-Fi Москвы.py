import csv

with open('wifi.csv', encoding='UTF-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    wifis = {}
    for row in rows:
        wifis[row['district']] = wifis.setdefault(row['district'], 0) + int(row['number_of_access_points'])
    for k, v in sorted(wifis.items(), key=lambda x: (-x[1], x[0])):
        print(f'{k}: {v}')