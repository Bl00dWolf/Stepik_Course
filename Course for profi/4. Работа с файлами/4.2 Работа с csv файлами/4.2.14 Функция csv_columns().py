import csv


def csv_columns(filename: str) -> dict:
    with open(filename, encoding='UTF=8') as file:
        rows = csv.DictReader(file)

        redict = {}
        for row in rows:
            for field in rows.fieldnames:
                redict.setdefault(field, []).append(row[field])
        return redict


# print(csv_columns('test.csv'))

# еще решение
# import csv
#
# def csv_columns(filename):
#
#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}