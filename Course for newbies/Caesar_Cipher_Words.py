string = input('Введите строку для шифрования\n').split()


def crypt_n_decrypt(string, delta, lang, choice):
    if lang.lower() == 'р':
        chars, mod = 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 32
    elif lang.lower() == 'а':
        chars, mod = 'abcdefghijklmnopqrstuvwxyz', 26

    if choice.lower() == 'р':
        delta = -delta

    for i in range(len(string)):
        if string[i] in '1234567890,./: !?"':
            continue

        if string[i].isupper():
            chartmp = chars.upper()[(chars.find(string[i].lower()) + delta) % mod]
        else:
            chartmp = chars.lower()[(chars.find(string[i].lower()) + delta) % mod]

        string = string[:i] + chartmp + string[i + 1:]
    return string


def crypt_word(word):
    real_len = 0
    for c in word:
        if c in ',."!?':
            real_len += 1
    real_len = len(word) - real_len

    return crypt_n_decrypt(word, real_len, 'а', 'ш')


for word in string:
    print(crypt_word(word), end=' ')
