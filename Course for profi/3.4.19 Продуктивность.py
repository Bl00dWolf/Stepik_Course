from datetime import datetime, timedelta

formatt = "%d.%m.%Y"
ddate = datetime.strptime(input(), formatt).date()

for i in range(1, 11):
    print(ddate.strftime(formatt))
    ddate += timedelta(days=(1 + i))
