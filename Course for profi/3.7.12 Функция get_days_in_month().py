import calendar
from datetime import datetime


def get_days_in_month(year: int, month: str) -> list[datetime.date]:
    monthh = list(calendar.month_name).index(month)
    days_in_month = calendar.monthrange(year, monthh)[1]
    return [datetime(year=year, month=monthh, day=i).date() for i in range(1, days_in_month + 1)]


# print(get_days_in_month(2021, 'December'))
