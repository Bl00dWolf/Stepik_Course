import json

with open('data.json', encoding='UTF-8') as file1:
    json_data = json.load(file1)

new_data = []
for elem in json_data:
    if isinstance(elem, str):
        new_data.append(elem + '!')
    elif isinstance(elem, bool):
        new_data.append(not elem)
    elif isinstance(elem, (int, float)):
        new_data.append(elem + 1)
    elif isinstance(elem, list):
        new_data.append(elem * 2)
    elif isinstance(elem, dict):
        elem['newkey'] = None
        new_data.append(elem)

with open('updated_data.json', 'w', encoding='UTF-8', newline='') as file2:
    json.dump(new_data, file2)
