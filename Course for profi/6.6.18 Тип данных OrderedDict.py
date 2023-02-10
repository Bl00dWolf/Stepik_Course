from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_list = []
for rule in range(len(data)):
    new_list.append(data.popitem(last=(rule % 2 != 0)))
print(OrderedDict(new_list))

# еще вариант
# data = OrderedDict([data.popitem(last=i & 1) for i in range(len(data))])