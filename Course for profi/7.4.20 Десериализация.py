import json

try:
    with open(input(), encoding='UTF-8') as file:
        print(json.load(file))
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')