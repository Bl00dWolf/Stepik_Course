import json
from datetime import datetime, timedelta


def is_right_day(x: dict) -> bool:
    """
    Возвращает True если словарь соот. условиям задачи - бассейн работает хотябы с 10ч до 12ч
    :param x: словарь с началом времени работы и концом
    :return: True если подходит по условию задачи (с 10 часов до 12 часов)
    """
    start_time = datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M')
    end_time = datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M')

    if timedelta(hours=start_time.hour, minutes=start_time.minute) - timedelta(hours=10) <= timedelta(
            seconds=0) and timedelta(hours=end_time.hour, minutes=end_time.minute) - timedelta(hours=12) > timedelta(
        seconds=0):
        return True
    return False


with open('pools.json', encoding='UTF8') as file:
    data = list(json.load(file))

# сортируем по длинне бассейна и по ширине.
data = sorted(filter(is_right_day, data), reverse=True,
              key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))

print(f"{data[0]['DimensionsSummer']['Length']}x{data[0]['DimensionsSummer']['Width']}\n{data[0]['Address']}")
