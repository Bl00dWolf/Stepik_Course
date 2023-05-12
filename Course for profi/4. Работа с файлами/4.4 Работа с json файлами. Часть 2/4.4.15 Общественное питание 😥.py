import json

with open('food_services.json', encoding='UTF-8') as file:
    data = list(json.load(file))

districts, op_comp = {}, {}

for dictt in data:
    districts[dictt['District']] = districts.setdefault(dictt['District'], 0) + 1
    if dictt['OperatingCompany']:
        op_comp[dictt['OperatingCompany']] = op_comp.setdefault(dictt['OperatingCompany'], 0) + 1

max_district = max(districts.items(), key=lambda x: x[1])
max_comp = max(op_comp.items(), key=lambda x: x[1])

print(f'{max_district[0]}: {max_district[1]}\n{max_comp[0]}: {max_comp[1]}')
