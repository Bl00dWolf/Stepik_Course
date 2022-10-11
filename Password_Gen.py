import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = digits

pass_num = int(input('Введите целое число - количество паролей для генерации: '))
pass_len = int(input('Введите целое число - длинну паролей: '))

pass_ABC = input('Должны ли быть в паролях прописные (большие) буквы? Д - да Н - нет\n')
pass_abc = input('Должны ли быть в паролях строчные (маленькие) буквы? Д - да Н - нет\n')
pass_specials = input('Должны ли быть в паролях специальные (!#$%&*+-=?@^_) символы? Д - да Н - нет\n')
pass_similar = input('Исключать ли неоднозначные символы (il1Lo0O) в паролях? Д - да Н - нет\n')

if pass_ABC.lower() == 'д':
    chars += uppercase_letters
if pass_abc.lower() == 'д':
    chars += lowercase_letters
if pass_specials.lower() == 'д':
    chars += punctuation
if pass_similar.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    random.seed()
    return [random.choice(chars) for _ in range(length)]


for i in range(pass_num):
    print(*generate_password(pass_len, chars), sep='')
