import locale
import calendar

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    elif not (0 <= number - 1 <= 6):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return calendar.day_name[number - 1].capitalize()

# print(get_weekday(1))