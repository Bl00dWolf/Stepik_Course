import calendar

year, month = input().split()
calendar.prmonth(int(year), list(calendar.month_abbr).index(month))
