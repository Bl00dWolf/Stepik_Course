class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def set_hours(self, hours: int):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    def get_hours(self):
        return self._hours

    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)
