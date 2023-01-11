with open('files.txt', encoding='UTF-8') as file:
    data = [s.strip().split() for s in file.readlines()]

data = sorted(data, key=lambda x: (x[0].split('.')[1], x[0]))  # ключ - формат файла, затем имя файла

data.append(data[-1])  # это костыль =\ иначе в цикле не переберется последний файл
size_sum = 0
for i in range(len(data) - 1):
    # все размеры преобразуем к B (bytes)
    if data[i][2].upper() == 'B':
        size_sum += int(data[i][1])
    elif data[i][2].upper() == 'KB':
        size_sum += int(data[i][1]) * 1024
    elif data[i][2].upper() == 'MB':
        size_sum += int(data[i][1]) * 1024 ** 2
    elif data[i][2].upper() == 'GB':
        size_sum += int(data[i][1]) * 1024 ** 3

    print(data[i][0])
    # если у вслед файла другое расширение или конец файла
    if data[i][0].split('.')[1] != data[i + 1][0].split('.')[1] or i == len(data) - 2:
        # перевод и округление к нужным величинам
        if size_sum <= 1024:
            print(f'----------\nSummary: {round(size_sum)} B\n')
        elif 1024 ** 2 >= size_sum > 1024:
            print(f'----------\nSummary: {round(size_sum / 1024)} KB\n')
        elif 1024 ** 3 >= size_sum > 1024 ** 2:
            print(f'----------\nSummary: {round(size_sum / (1024 ** 2))} MB\n')
        elif size_sum > 1024 ** 3:
            print(f'----------\nSummary: {round(size_sum / (1024 ** 3))} GB\n')
        size_sum = 0

# еще решение
# dict_names = {}
# dict_size = {}
# dict_dimension = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
# with open("files.txt", 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         # разделяем на нужные нам слова
#         name, size, dimension = line.split()
#         name, extension = name.split('.')
#         # заполняем словарь с именами по расширениям
#         dict_names[extension] = (dict_names.get(extension, []) +
#                                  [name + '.' + extension])
#         # заполняем словарь с размерами по расширениям
#         dict_size[extension] = (dict_size.get(extension, 0) +
#                                  dict_dimension[dimension] * int(size))
#
#     for extension in sorted(dict_names):
#         print(*sorted(dict_names[extension]), sep='\n')
#         print('----------')
#         for key in dict_dimension:
#             result = dict_size[extension] / dict_dimension[key]
#             if result <= 1024:
#                 break
#         print('Summary:', round(result), key)
#         print()