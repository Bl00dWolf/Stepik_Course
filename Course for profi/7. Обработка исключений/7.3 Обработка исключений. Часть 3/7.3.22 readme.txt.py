try:
    with open(input(), encoding='UTF-8') as file:
        for line in file.readlines():
            print(line.strip())
except FileNotFoundError:
    print('Файл не найден')

# еще варик
# try:
#     with open(input(), encoding="utf-8") as file:
#         print(file.read())
# except:
#     print("Файл не найден")