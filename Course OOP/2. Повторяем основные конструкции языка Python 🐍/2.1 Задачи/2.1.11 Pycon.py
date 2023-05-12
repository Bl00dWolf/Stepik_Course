from datetime import datetime
import calendar

year, month = int(input()), int(input())

calendar.setfirstweekday(calendar.THURSDAY)
if calendar.monthcalendar(year, month)[0][0] == 0:
    day = calendar.monthcalendar(year, month)[4][0]
else:
    day = calendar.monthcalendar(year, month)[3][0]

print(datetime(year, month, day).date().strftime('%d.%m.%Y'))

# еще вариант:
# from datetime import date
#
# year, month = int(input()), int(input())
#
# for i in range(1, 8):
#     if date(year, month, i).isoweekday() == 4:
#         day = i + 21
#
# print(date(year, month, day).strftime('%d.%m.%Y'))