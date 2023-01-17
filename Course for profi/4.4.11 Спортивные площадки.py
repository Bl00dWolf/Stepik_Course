import json
import csv

with open('playgrounds.csv', encoding='UTF-8') as file1:
    reader = csv.DictReader(file1, delimiter=';')
    field_names = reader.fieldnames
    data = list(reader)

new_data = {}
for dictt in data:
    new_data.setdefault(dictt['AdmArea'], {dictt['District']: []})
    new_data[dictt['AdmArea']].setdefault(dictt['District'], []).append(dictt['Address'])

with open('addresses.json', 'w', encoding='UTF-8', newline='') as file2:
    json.dump(new_data, file2, indent=3, ensure_ascii=False)

# еще вариант решения
# import json, csv
#
# with open('playgrounds.csv', encoding='utf-8') as fin, \
#     open('addresses.json', 'w', encoding='utf-8') as fout:
#     pgs = list(csv.reader(fin, delimiter=';'))[1:]
#
#     districts = {}
#     for name, area, district, addr in pgs:
#         districts.setdefault(area, {}).setdefault(district,[]).append(addr)
#
#     json.dump(districts, fout, indent=3, ensure_ascii=False)
