import csv

with open('titanic.csv', encoding='UTF-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    females = []
    for row in rows:
        if float(row['age']) < 18.0 and row['survived'] == '1':
            if row['sex'] == 'male':
                print(row['name'])
            elif row['sex'] == 'female':
                females.append(row['name'])
    print(*females, sep='\n')