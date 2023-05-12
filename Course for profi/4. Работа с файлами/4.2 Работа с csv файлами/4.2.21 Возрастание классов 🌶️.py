import csv

with open('student_counts.csv', encoding='UTF-8') as file1:
    reader = csv.DictReader(file1)
    classes = list(reader)
    field_names = sorted(reader.fieldnames[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    field_names.insert(0, reader.fieldnames[0])

with open('sorted_student_counts.csv', 'w', encoding='UTF-8', newline='') as file2:
    writter = csv.DictWriter(file2, fieldnames=field_names)
    writter.writeheader()
    writter.writerows(classes)
