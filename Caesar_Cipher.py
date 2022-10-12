choice = input('Шифр Цезаря\nЧто вы хотите сделать с текстом? Ш - шифровать Д - расшифровать\n')
lang = input('Какой язык текста будет использован? Р - русский А - английский\n')
delta = int(input('Задайте шаг сдвига (целое число)\n'))

chars_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
chars_eng = 'abcdefghijklmnopqrstuvwxyz'


def crypt(string, delta):
    for i in range(len(string)):
        if string[i] in '1234567890,./: !?':
            continue

        if string[i].isupper():
            chartmp = chars_ru.upper()[(chars_ru.find(string[i].lower()) + delta) % 32]
        else:
            chartmp = chars_ru.lower()[(chars_ru.find(string[i].lower()) + delta) % 32]

        string = string[:i] + chartmp + string[i + 1:]
    return string


if choice.lower() == 'ш':
    print(crypt(input('Введите текст для расшифровки\n'), delta))
