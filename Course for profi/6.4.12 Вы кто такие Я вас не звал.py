from collections import namedtuple
import csv
from datetime import datetime

with open('meetings.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file))
    fields = list(data[0].keys())

pers_met = namedtuple('pers_met', fields)

new_data = []
for dic in data:
    day, month, year, hour, minute = int(dic['meeting_date'].split('.')[0]), int(
        dic['meeting_date'].split('.')[1]), int(dic['meeting_date'].split('.')[2]), int(
        dic['meeting_time'].split(':')[0]), int(dic['meeting_time'].split(':')[1])
    ddate = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    new_data.append(pers_met(dic['surname'], dic['name'], ddate.date(), ddate.time()))

for person in sorted(new_data, key=lambda x: (x.meeting_date, x.meeting_time)):
    print(f'{person.surname} {person.name}')
