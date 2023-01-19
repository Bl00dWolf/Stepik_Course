import json
from datetime import datetime, timedelta


def is_right_day(x: dict) -> bool:
    start_time = datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M')
    end_time = datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M')

    if timedelta(hours=start_time.hour, minutes=start_time.minute) - timedelta(hours=10) <= timedelta(
                seconds=0) and  timedelta(hours=end_time.hour, minutes=end_time.minute) - timedelta(hours=12) > timedelta(
                seconds=0):
        return True
    return False


with open('pools.json', encoding='UTF8') as file:
    data = list(json.load(file))

data = list(filter(is_right_day, data))
print(*data, sep='\n')
