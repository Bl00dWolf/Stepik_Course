from datetime import datetime

birtdays = dict()
date_count = dict()
for _ in range(int(input())):
    s = input().split()
    birtdays[datetime.strptime(s[2], '%d.%m.%Y').date()] = s[0] + ' ' + s[1]
    date_count[datetime.strptime(s[2], '%d.%m.%Y').date()] = date_count.setdefault(
        datetime.strptime(s[2], '%d.%m.%Y').date(), 0) + 1

dates_more_one = list(filter(lambda x: x[1] > 1, date_count.items()))
if len(dates_more_one) > 0:
    print(f'{sorted(dates_more_one, key=lambda x: x[1])[0][0].strftime("%d.%m.%Y")} {sorted(dates_more_one, key=lambda x: x[1])[0][1]}')
else:
    print(f'{sorted(birtdays.items(), key=lambda x: x[0])[0][0].strftime("%d.%m.%Y")} {sorted(birtdays.items(), key=lambda x: x[0])[0][1]}')