import json
import csv

with open('students.json', encoding='UTF-8') as fro:
    data = list(json.load(fro))

data = list(filter(lambda x: x['progress'] >= 75 and x['age'] >= 18, sorted(data, key=lambda x: x['name'])))

with open('data.csv', 'w', encoding='UTF-8', newline='') as fwr:
    writterr = csv.DictWriter(fwr, fieldnames=['name', 'phone'], extrasaction='ignore')
    writterr.writeheader()
    for dictt in data:
        writterr.writerow(dictt)
