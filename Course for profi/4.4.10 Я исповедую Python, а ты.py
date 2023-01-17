import json

with open('countries.json', encoding='UTF-8') as file1:
    data = json.load(file1)

new_data = {}
for ddict in data:
    new_data.setdefault(ddict['religion'], []).append(ddict['country'])

with open('religion.json', 'w', encoding='UTF-8', newline='') as file2:
    json.dump(new_data, file2, indent=3)