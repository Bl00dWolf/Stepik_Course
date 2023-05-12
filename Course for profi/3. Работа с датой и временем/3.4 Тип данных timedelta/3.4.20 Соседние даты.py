from datetime import datetime, timedelta

ddates = [datetime.strptime(d, '%d.%m.%Y').date() for d in input().split()]

for i in range(len(ddates) - 1):
    ddates[i] = abs((ddates[i + 1] - ddates[i]).days)
del ddates[-1]

print(ddates)
