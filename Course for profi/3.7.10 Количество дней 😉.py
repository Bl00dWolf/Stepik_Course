import calendar

year, month = list(map(int, input().split()))
print(calendar.monthrange(year, month)[1])