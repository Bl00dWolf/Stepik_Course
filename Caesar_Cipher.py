choice = input('Шифр Цезаря\nЧто вы хотите сделать с текстом? Ш - шифровать Д - расшифровать\n')
lang = input('Какой язык текста будет использован? Р - русский А - английский\n')
delta = int(input('Задайте шаг сдвига (целое число)\n'))

chars_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
chars_eng = 'abcdefghijklmnopqrstuvwxyz'


def crypt(string, delta):
    for c in string:
        if c in '1234567890,./: !?':
            continue
        string = string.lower().replace(c, chars_ru[(chars_ru.find(c) + delta) % 32])
    return string


if choice.lower() == 'ш':
    print(crypt(input('Введите текст для расшифровки\n'), delta))
