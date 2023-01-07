import csv

with open('data.csv', encoding='UTF-8') as file1:
    rows = csv.DictReader(file1)
    domains = {}
    for row in rows:
        domain = row['email'].split('@')[1]
        domains[domain] = domains.setdefault(domain, 0) + 1

with open('domain_usage.csv', 'w', encoding='UTF-8', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(['domain', 'count'])
    for row in sorted(sorted(domains.items()), key=lambda x: x[1]):
        writer.writerow(row)
