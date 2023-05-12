from datetime import datetime

chk_dates = datetime.strptime(input(), '%d.%m.%Y').date().toordinal()
chk_dates = [datetime.fromordinal(d).date() for d in range(chk_dates + 1, chk_dates + 7 + 1)]

birtdays = dict()
for _ in range(int(input())):
    *name, ddate = input().split()
    birtdays[datetime.strptime(ddate, '%d.%m.%Y').date()] = ' '.join(name)

listek = []
for ddate in birtdays.keys():
    for chk_date in chk_dates:
        if ddate == chk_date.replace(year=ddate.year):
            listek.append(ddate)
print(birtdays[max(listek)]) if listek else print('Дни рождения не планируются')
