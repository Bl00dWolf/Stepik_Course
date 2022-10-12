choice = input('Шифр Цезаря\nЧто вы хотите сделать с текстом? Ш - шифровать Д - расшифровать\n')
lang = input('Какой язык текста будет использован? Р - русский А - английский\n')
delta = int(input('Задайте шаг сдвига (целое число)\n'))

chars_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
chars_eng = 'abcdefghijklmnopqrstuvwxyz'


def crypt(string, delta):
    if lang.lower() == 'р':
        chars, mod = chars_ru, 32
    elif lang.lower() == 'а':
        chars, mod = chars_eng, 26

    for i in range(len(string)):
        if string[i] in '1234567890,./: !?':
            continue

        if string[i].isupper():
            chartmp = chars.upper()[(chars.find(string[i].lower()) + delta) % mod]
        else:
            chartmp = chars.lower()[(chars.find(string[i].lower()) + delta) % mod]

        string = string[:i] + chartmp + string[i + 1:]
    return string


if choice.lower() == 'ш':
    print(crypt(input('Введите текст для расшифровки\n'), delta))
