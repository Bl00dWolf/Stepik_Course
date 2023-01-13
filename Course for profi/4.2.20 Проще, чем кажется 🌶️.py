import csv


def condense_csv(filename: str, id_name: str) -> None:
    with open(filename, encoding='UTF-8') as file1:
        items, params, values = [], [id_name], []
        for line in file1.readlines():
            obj_line = line.strip().split(',')  # разбиваем строку по запятым
            if obj_line[0] not in items:  # проверяем, что этого предмета еще нет в списке
                items.append(obj_line[0])  # первая часть это сам предмет
            if obj_line[1] not in params:  # проверяем что этого параметра еще нет в списке
                params.append(obj_line[1])  # вторая часть это название параметра
            values.append(obj_line[2])  # третья часть это сам параметр

    with open('condensed.csv', 'w', encoding='UTF-8', newline='') as file2:
        writer = csv.writer(file2)
        writer.writerow(params)  # записываем название колонок в файл
        for item in items:
            vals = []
            # каждый раз заносим значение в лист значений для текущего предмета и удаляем из исходного списка
            for _ in range(len(params) - 1):
                vals.append(values[0])
                values.pop(0)
            writer.writerow([item, *vals])


condense_csv('data.csv', 'ID_Obj')

# Еще вариант решения
# import csv
#
#
# def condense_csv(filename, id_name):
#     with open(filename, encoding='utf-8') as file:
#         objects = {}
#         for obj, attr, value in csv.reader(file):
#             if obj not in objects:
#                 objects[obj] = {id_name: obj}
#             objects[obj][attr] = value
#
#     with open('condensed.csv', 'w', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=objects[obj])
#         writer.writeheader()
#         writer.writerows(objects.values())
