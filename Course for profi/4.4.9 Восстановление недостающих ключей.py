import json

with open('people.json', encoding='UTF-8') as file1:
    data = json.load(file1)

kkeys = set()
[kkeys.update(dictt.keys()) for dictt in data]

new_data = []
for dictt in data:
    for kkey in kkeys:
        dictt[kkey] = dictt.setdefault(kkey, None)
    new_data.append(dictt)


with open('updated_people.json', 'w', encoding='UTF-8', newline='') as file2:
    json.dump(new_data, file2, indent=3, sort_keys=True)

# Еще решение
# import json
#
# with open('people.json', encoding='utf8') as fi, open('updated_people.json', 'w') as fo:
#     people = json.load(fi)
#     d = {k: None for i in people for k in i.keys()}
#     json.dump([d | i for i in people], fo)