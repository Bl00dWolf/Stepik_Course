import csv

with open('salary_data.csv', encoding='UTF-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    companies = {}
    for row in rows:
        companies.setdefault(row['company_name'], []).append(int(row['salary']))
    for k, v in companies.items():
        companies[k] = sum(v) / len(v)

print(*sorted(sorted(companies), key=lambda x: companies.get(x)), sep='\n')
