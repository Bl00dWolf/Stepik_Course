import calendar

year, month, day = list(map(lambda x: int(x), input().split('-')))
print(calendar.day_name[calendar.weekday(year, month, day)])

# Еще решение
# import calendar
# from datetime import datetime
#
# dt = datetime.fromisoformat(input())
#
# print(list(calendar.day_name)[dt.weekday()])

