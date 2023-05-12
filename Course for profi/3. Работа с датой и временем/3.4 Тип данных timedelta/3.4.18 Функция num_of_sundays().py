from datetime import datetime


def num_of_sundays(year: int) -> int:
    return len([i for i in range(datetime(year=year, month=1, day=1).date().toordinal(),
                                 datetime(year=year, month=12, day=31).date().toordinal() + 1) if
                datetime.fromordinal(i).weekday() == 6])


print(num_of_sundays(2021))
print(num_of_sundays(2000))

# Еще вариант
# from datetime import date
#
# def num_of_sundays(year):
#     return date(year, 12, 31).strftime('%U')