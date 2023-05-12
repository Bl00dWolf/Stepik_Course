def years_days(year: int):
    from datetime import datetime, date
    start = datetime.toordinal(date(day=1, month=1, year=year))
    end = datetime.toordinal(date(day=31, month=12, year=year))
    return (date.fromordinal(i) for i in range(start, end + 1))

# еще вариант
# from datetime import date, timedelta
#
# def years_days(year: int):
#     start = date(year, 1, 1)
#     while start.year == year:
#         yield start
#         start += timedelta(days=1)

# dates = years_days(2022)
#
# print(next(dates))
# print(next(dates))
# print(next(dates))
# print(next(dates))

