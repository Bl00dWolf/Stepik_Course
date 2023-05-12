from datetime import datetime, timedelta

formatt = '%H:%M'
start_time, end_time = datetime.strptime(input(), formatt), datetime.strptime(input(), formatt)

if abs(end_time - start_time) > timedelta(minutes=45):
    delta_time = start_time
    while delta_time + timedelta(minutes=45) <= end_time:
        delta_time_str = datetime.strftime(delta_time, formatt)
        lesson_time_str = datetime.strftime(delta_time + timedelta(minutes=45), formatt)
        print(f'{delta_time_str} - {lesson_time_str}')
        delta_time += timedelta(minutes=55)
