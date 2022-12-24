from datetime import datetime, timedelta


def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])


rs_date = datetime(year=2022, month=11, day=8, hour=12, minute=0)
cur_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
dif_date = rs_date - cur_date

if dif_date > timedelta(seconds=0):
    print(f'До выхода курса осталось: {choose_plural(dif_date.days)}')  # фигня с этого момента продолжи
else:
    print('Курс уже вышел!')
