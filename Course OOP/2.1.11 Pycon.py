from datetime import datetime
import calendar

year, month = int(input()), int(input())
# year, month = 2012, 3


ddate = calendar.monthcalendar(year=year, month=month)[3][3]
while ddate == 0:
    month += 1
    ddate = calendar.monthcalendar(year=year, month=month)[3][3]
print(datetime.strptime(f'{ddate}.{month}.{year}', '%d.%m.%Y').date().strftime('%d.%m.%Y'))
