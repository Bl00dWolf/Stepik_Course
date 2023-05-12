import json

with open('data1.json', encoding='UTF-8') as file1, open('data2.json', encoding='UTF-8') as file2:
    data1, data2 = json.load(file1), json.load(file2)

data1.update(data2)

with open('data_merge.json', 'w', encoding='UTF-8', newline='') as file3:
    json.dump(data1, file3)

# еще вариант
# import json
#
# with open('data1.json', encoding='Utf-8') as file1, \
#         open('data2.json', encoding='utf-8') as file2, \
#         open('data_merge.json', 'w') as outer:
#     data1, data2 = json.load(file1), json.load(file2)
#     json.dump(data1 | data2, outer)
