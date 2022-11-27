import random

num_r, num, count = random.randint(1, 100), -999, 0


def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    return False


print('Добро пожаловать в числовую угадайку')

while num != num_r:
    num = input()

    if is_valid(num):
        num = int(num)
        count += 1
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    if num > num_r:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif num < num_r:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num == num_r:
        print(f'Вы угадали, поздравляем! Загаданное число - {num_r}\nВы отгадали число с {count} попыток.')
        print('\nХотите сыграть еще раз? Д - да, Н - нет')
        if input().lower() == 'д':
            num_r, count = random.randint(1, 100), 0
            continue
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
