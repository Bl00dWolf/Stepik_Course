from datetime import date
import calendar


def get_all_mondays(year: int) -> [date]:
    start, end = date(year, 1, 1).toordinal(), date(year, 12, 31).toordinal() + 1
    return [date.fromordinal(i) for i in range(start, end) if date.fromordinal(i).weekday() == 0]

# print(get_all_mondays(2021))
# >> [datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]

# решение через календарь
# def get_all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             monday = week[0]
#             if monday:
#                 mondays.append(date(year, month, monday))
#     return mondays
