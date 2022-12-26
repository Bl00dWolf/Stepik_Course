import sys
from datetime import date

dates = [date.fromisoformat(d.strip('\n')) for d in sys.stdin.readlines()]
dates = [min(dates), max(dates)]

print(dates[1].toordinal() - dates[0].toordinal())