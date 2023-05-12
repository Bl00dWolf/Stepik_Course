from datetime import date


def saturdays_between_two_dates(start, end):
    if start <= end:
        return sum([1 for d in range(start.toordinal(), end.toordinal() + 1) if date.fromordinal(d).weekday() == 5])
    elif start >= end:
        return sum([1 for d in range(end.toordinal(), start.toordinal() + 1) if date.fromordinal(d).weekday() == 5])
    return 0


# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))
#
# date1 = date(2020, 7, 26)
# date2 = date(2020, 7, 2)
#
# print(saturdays_between_two_dates(date1, date2))
#
# date1 = date(2018, 7, 13)
# date2 = date(2018, 7, 13)
#
# print(saturdays_between_two_dates(date1, date2))