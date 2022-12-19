from datetime import datetime, timedelta

d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

start_date, end_date = datetime(year=1, month=1, day=1).toordinal(), datetime(year=9999, month=12, day=31).toordinal()

for year in range(1, 9999 + 1):
    for month in range(1, 12 + 1):
        d[datetime(year=year, month=month, day=13).weekday()] += 1
print(*d.values(), sep='\n')
