from datetime import timedelta
from enum import IntEnum

Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        next_date = self.today + timedelta((self.weekday - self.today.weekday()) % 7)
        if not self.after_today and next_date == self.today:
            next_date += timedelta(7)
        return next_date

    def days_until(self):
        return (self.date() - self.today).days
