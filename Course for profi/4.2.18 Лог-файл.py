import csv
from datetime import datetime

with open('name_log.csv', encoding='UTF-8') as file1:
    rows = csv.DictReader(file1)

    user_dates = {}
    for row in rows:
        user_dates.setdefault(row['email'], []).append(
            (row['username'], datetime.strptime(row['dtime'], '%d/%m/%Y %H:%M')))

with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(rows.fieldnames)

    for k, v in sorted(user_dates.items()):
        username, ddate = max(v, key=lambda x: x[1])
        writer.writerow([username, k, ddate.strftime('%d/%m/%Y %H:%M')])

# еще решение
# import csv
# from datetime import datetime
#
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)
#
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))