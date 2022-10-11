choice = input('Шифр Цезаря\nЧто вы хотите сделать с текстом? Ш - шифровать Д - расшифровать')
lang = input('Какой язык текста будет использован? Р - русский А - английский')
delta = int(input('Задайте шаг сдвига (целое число)'))

chars_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
chars_eng = 'abcdefghijklmnopqrstuvwxyz'


def crypt(string, delta):
    for c in string:
        string = string.replace(c, chr(ord(c) + delta))
    return string


if choice.lower() == 'ш':
    print(crypt(input('Введите текст для расшифровки\n'), delta))
