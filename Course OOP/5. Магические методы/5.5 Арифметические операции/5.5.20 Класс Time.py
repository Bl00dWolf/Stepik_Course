class Time:
    def __init__(self, hours: int, minutes: int):
        while minutes >= 60:
            minutes -= 60
            hours += 1
        hours %= 24

        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        if self.hours < 10:
            hrs = '0' + str(self.hours)
        else:
            hrs = self.hours

        if self.minutes < 10:
            mnt = '0' + str(self.minutes)
        else:
            mnt = self.minutes
        return f'{hrs}:{mnt}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.hours += other.hours
            self.minutes += other.minutes

            while self.minutes >= 60:
                self.minutes -= 60
                self.hours += 1
            self.hours %= 24

            return self
        return NotImplemented

# еще вариант
#
# 
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours, self.minutes = Time._normalize(hours, minutes)
#
#     @staticmethod
#     def _normalize(hours, minutes):
#         return (hours + minutes // 60) % 24, minutes % 60
#
#     def __str__(self):
#         return f'{self.hours:>02}:{self.minutes:>02}'
#
#     def __add__(self, other):
#         if isinstance(other, Time):
#             hours, minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
#             return Time(hours, minutes)
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, Time):
#             self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
#             return self
#         return NotImplemented
#
