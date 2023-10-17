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
        if not self.after_today:
            dday = self.today.weekday() + 1
            ddate = self.today + timedelta(days=1)
        else:
            dday = self.today.weekday()
            ddate = self.today

        while dday != self.weekday.value:
            if dday > 6:
                dday = -1
            dday += 1
            ddate += timedelta(days=1)
        return ddate

    def days_until(self) -> int:
        if not self.after_today:
            dday = self.today.weekday() + 1
        else:
            dday = self.today.weekday()

        while dday != self.weekday.value:
            if dday > 6:
                dday = -1
            dday += 1
        return dday


today = date(2023, 4, 17)  # понедельник
next_monday = NextDate(today, Weekday.MONDAY)  # следующий понедельник без учета текущего

print(next_monday.date())
print(next_monday.days_until())
