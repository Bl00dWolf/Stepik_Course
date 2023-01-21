import json

with open('food_services.json', encoding='UTF-8') as file:
    data = list(json.load(file))

types_obj = {}
for dictt in data:
    if dictt['Name']:
        types_obj.setdefault(dictt['TypeObject'], [])
        types_obj[dictt['TypeObject']].append((dictt['Name'], dictt['SeatsCount']))

for k in sorted(types_obj.keys()):
    types_obj[k] = max(types_obj[k], key=lambda x: x[1])

for category, values in sorted(types_obj.items()):
    print(f'{category}: {values[0]}, {values[1]}')


# еще решение
# import json
#
# with open('food_services.json', 'r', encoding='utf-8') as f1:
#     data = json.load(f1)
#     d = {i['TypeObject']: f"{i['Name']}, {i['SeatsCount']}" for i
#          in sorted(data, key=lambda x:(x['TypeObject'], x['SeatsCount']))}
#     for item in d.items():
#         print(f'{item[0]}: {item[1]}')
