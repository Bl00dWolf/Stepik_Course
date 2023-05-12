from datetime import date, time


def print_good_dates(dates):
    new_d = []
    for d in dates:
        if d.year == 1992 and d.month + d.day == 29:
            new_d.append(d)
    new_d.sort()
    [print(d.strftime('%B %d, %Y')) for d in new_d]


# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)

# еще вариант решения
# def print_good_dates(dates):
#     for d in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates)):
#         print(d.strftime('%B %d, %Y'))