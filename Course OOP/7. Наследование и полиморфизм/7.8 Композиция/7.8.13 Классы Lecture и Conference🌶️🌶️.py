from datetime import datetime, timedelta


class Lecture:
    def __init__(self, topic: str, start_time: str, duration: str):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.duration = datetime.strptime(duration, '%H:%M')
        self.end_time = datetime.strptime(start_time, '%H:%M') + timedelta(hours=self.duration.hour,
                                                                           minutes=self.duration.minute)


class Conference:
    def __init__(self):
        self._conferences_ = []

    def add(self, new_lecture: Lecture) -> None:
        for lecture in self._conferences_:
            cond1 = lecture.start_time <= new_lecture.start_time < lecture.end_time
            cond2 = new_lecture.start_time <= lecture.start_time < new_lecture.end_time
            if cond1 or cond2:
                raise ValueError('Провести выступление в это время невозможно')
        self._conferences_.append(new_lecture)

    def total(self):
        total = int(sum(
            [timedelta(hours=lecture.duration.hour, minutes=lecture.duration.minute).total_seconds() for lecture in
             self._conferences_]))
        total = list(map(lambda x: f'{x:>02}', str(timedelta(seconds=total)).split(':')))[:2]
        return ':'.join(total)

    def longest_lecture(self):
        max_long = max(self._conferences_, key=lambda x: x.duration)
        return max_long.duration.strftime('%H:%M')

    def longest_break(self):
        confs = sorted(self._conferences_, key=lambda x: x.start_time)
        max_sec = timedelta(seconds=0)
        for i in range(len(confs) - 1):
            if confs[i + 1].start_time - confs[i].end_time > max_sec:
                max_sec = confs[i + 1].start_time - confs[i].end_time
        max_sec = list(map(lambda x: f'{x:>02}', str(max_sec).split(':')))[:2]
        return ':'.join(max_sec)

# Еще решение
# from bisect import insort
# from datetime import datetime, timedelta
#
# from dateutil.relativedelta import relativedelta
#
#
# class Lecture:
#     _PATTERN = '%H:%M'
#
#     def __init__(self, topic, start_time, duration):
#         self.topic = topic
#         self.start_time = datetime.strptime(start_time, self._PATTERN)
#         self.duration = datetime.strptime(duration, self._PATTERN)
#         self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)
#
#
# class Conference:
#     def __init__(self):
#         self.lectures = []
#
#     def add(self, lecture):
#         for cur_lecture in self.lectures:
#             if any((
#                     cur_lecture.start_time <= lecture.start_time < cur_lecture.end_time,
#                     lecture.start_time <= cur_lecture.start_time < lecture.end_time,
#             )):
#                 raise ValueError('Провести выступление в это время невозможно')
#         insort(self.lectures, lecture, key=lambda item: item.start_time)
#
#     def total(self):
#         total = sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=relativedelta())
#         return f'{total.hours:0>2}:{total.minutes:0>2}'
#
#     def longest_lecture(self):
#         longest = max(lecture.duration for lecture in self.lectures)
#         return f'{longest.hour:0>2}:{longest.minute:0>2}'
#
#     def longest_break(self):
#         longest = max(self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1))
#         hours, minutes = int(longest.total_seconds()) // 3600, (int(longest.total_seconds()) // 60) % 60
#         return f'{hours:0>2}:{minutes:0>2}'
