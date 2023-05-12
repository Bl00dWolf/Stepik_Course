from datetime import datetime, timedelta
formatt = '%d.%m.%Y'
ddates = [datetime.strptime(input(), formatt).date(), datetime.strptime(input(), formatt).date()]

st_date = 0
for i in range(ddates[0].toordinal(), ddates[1].toordinal() + 1):
    if (datetime.fromordinal(i).day + datetime.fromordinal(i).month) % 2 > 0:
        st_date = datetime.fromordinal(i).date()
        break

for i in range(st_date.toordinal(), ddates[1].toordinal() + 1, 3):
    if datetime.fromordinal(i).weekday() not in [0, 3]:
        print(datetime.fromordinal(i).strftime(formatt))

# еще решение
# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# start = datetime.strptime(input(), pattern)
# end = datetime.strptime(input(), pattern)
#
# while not (start.month + start.day) % 2:
#     start += timedelta(days=1)
#
# while start <= end:
#     week = start.isoweekday()
#     if week in (2,3,5,6,7):
#         print(start.strftime(pattern))
#     start += timedelta(days=3)