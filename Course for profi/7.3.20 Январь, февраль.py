import calendar

month = {k: v for k, v in enumerate(calendar.month_name[1:], 1)}

try:
    print(month[int(input())])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
