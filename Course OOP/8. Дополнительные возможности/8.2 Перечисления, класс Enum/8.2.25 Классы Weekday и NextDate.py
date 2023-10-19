from enum import Enum
from datetime import datetime, date, timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today: date, weekday: Weekday, after_today: bool = False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self) -> date:
        cur_dat = self.today
        if self.after_today:
            cur_dat = self.today - timedelta(days=self.weekday.value)
        elif cur_dat.weekday() == self.weekday.value:
            cur_dat += timedelta(days=1)
        while cur_dat.weekday() != self.weekday.value:
            cur_dat += timedelta(days=1)
        return cur_dat

    def days_until(self) -> int:
        count = 0
        cur_dat = self.today
        if self.after_today:
            cur_dat = self.today - timedelta(days=self.weekday.value)
        elif cur_dat.weekday() == self.weekday.value:
            cur_dat += timedelta(days=1)
            count += 1
        while cur_dat.weekday() != self.weekday.value:
            cur_dat += timedelta(days=1)
            count += 1
        return count


# today = date(2023, 4, 17)                              # понедельник
# next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница
#
# print(next_friday.date())
# print(next_friday.days_until())
#
# today = date(2023, 4, 17)                              # понедельник
# next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета текущего
#
# print(next_monday.date())
# print(next_monday.days_until())
#
# today = date(2023, 4, 17)                              # понедельник
# next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом текущего
#
# print(next_monday.date())
# print(next_monday.days_until())

for weekday in Weekday:
    today = date(2023, 4, 27)                              # четверг
    next_date = NextDate(today, weekday, True)

    print(next_date.date())
    print(next_date.days_until())