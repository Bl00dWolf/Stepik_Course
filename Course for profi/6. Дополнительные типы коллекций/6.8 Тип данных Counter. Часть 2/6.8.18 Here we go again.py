from collections import Counter
import csv

with open('name_log.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file))

lg_changes = Counter()
for ddict in data:
    lg_changes[ddict['email']] += 1

[print(f'{email}: {num}') for email, num in sorted(lg_changes.items())]