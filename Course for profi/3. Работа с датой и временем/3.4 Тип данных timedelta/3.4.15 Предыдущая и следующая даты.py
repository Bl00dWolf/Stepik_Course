from datetime import datetime, timedelta

ddate = datetime.strptime(input(), '%d.%m.%Y').date()
print(datetime.strftime(ddate - timedelta(days=1), '%d.%m.%Y'))
print(datetime.strftime(ddate + timedelta(days=1), '%d.%m.%Y'))