import calendar
from datetime import date

year = int(input())
dates = []
for month in range(1, 12 + 1):
    if not calendar.monthcalendar(year, month)[0][3]:
        wk_third_chet = calendar.monthcalendar(year, month)[3][3]
    else:
        wk_third_chet = calendar.monthcalendar(year, month)[2][3]
    if wk_third_chet:
        dates.append(date(year, month, wk_third_chet))

[print(date.strftime("%d.%m.%Y")) for date in sorted(dates)]
