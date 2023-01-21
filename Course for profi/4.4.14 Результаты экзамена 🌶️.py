from datetime import datetime, timedelta
import json
import csv

with open('exam_results.csv', encoding='UTF-8') as flro:
    readder = csv.DictReader(flro)
    data = list(readder)

for dictt in data:
    dictt['score'] = int(dictt['score'])
data = sorted(data, reverse=True, key=lambda x: datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S'))
data = sorted(data, key=lambda x: (x['email'], -x['score']))

listed, new_data = [], []
for dictt in data:
    if dictt['email'] not in listed:
        listed.append(dictt['email'])
        new_data.append({'name': dictt['name'], 'surname': dictt['surname'], 'best_score': dictt['score'],
                         'date_and_time': dictt['date_and_time'], 'email': dictt['email']})

with open('best_scores.json', 'w', encoding='UTF-8', newline='') as flwr:
    json.dump(new_data, flwr, indent=3)

# еще вариант
# import json, csv
#
# with open('exam_results.csv', encoding='utf8') as file:
#     head, *rows = list(csv.reader(file, delimiter=','))
#
# rows.sort(key=lambda x: x[2])  # sort by score
# rows.sort(key=lambda x: x[3])  # sort by time
# rows.sort(key=lambda x: x[4])  # sort by email
#
# data = {}
# for name, surname, score, date_and_time, email in rows:
#     data[email] = {'name': name, 'surname': surname, 'best_score': int(score),
#                    'date_and_time': date_and_time, 'email': email}
#
# with open('best_scores.json', 'w', encoding='utf8') as file:
#     json.dump(list(data.values()), file, indent=3)
