from datetime import datetime, timedelta, time

curd = datetime.strptime(input(), "%d.%m.%Y %H:%M")

if curd.strftime('%w') in '12345' and time(hour=9) <= curd.time() < time(hour=21):
    print(int((timedelta(hours=21) - timedelta(hours=curd.hour, minutes=curd.minute)).total_seconds()) // 60)
elif curd.strftime('%w') in '06' and time(hour=10) <= curd.time() < time(hour=18):
    print(int((timedelta(hours=18) - timedelta(hours=curd.hour, minutes=curd.minute)).total_seconds()) // 60)
else:
    print('Магазин не работает')

# еще решение
# from datetime import datetime, timedelta, time
# 
# curd = datetime.strptime(input(), "%d.%m.%Y %H:%M")
#
# if curd.strftime('%w') in '12345' and time(hour=9) <= curd.time() < time(hour=21):
#     print(int((timedelta(hours=21) - timedelta(hours=curd.hour, minutes=curd.minute)).total_seconds()) // 60)
# elif curd.strftime('%w') in '06' and time(hour=10) <= curd.time() < time(hour=18):
#     print(int((timedelta(hours=18) - timedelta(hours=curd.hour, minutes=curd.minute)).total_seconds()) // 60)
# else:
#     print('Магазин не работает')