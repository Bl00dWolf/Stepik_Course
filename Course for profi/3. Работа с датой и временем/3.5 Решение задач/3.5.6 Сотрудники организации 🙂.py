from datetime import datetime

date_count = dict()
for _ in range(int(input())):
    s = input().split()
    date_count[datetime.strptime(s[2], '%d.%m.%Y').date()] = date_count.setdefault(
        datetime.strptime(s[2], '%d.%m.%Y').date(), 0) + 1

fin_dates = list(filter(lambda x: x[1] == max(date_count.values()), sorted(date_count.items(), key=lambda x: x[1], reverse=True)))

for d in sorted(fin_dates):
    print(d[0].strftime('%d.%m.%Y'))