from datetime import date, timedelta


def dates(start: date, count: int = None):
    if not count:
        count = -1
    while count:
        count -= 1
        yield start
        try:
            start += timedelta(days=1)
        except OverflowError:
            break