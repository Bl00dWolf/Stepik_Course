from datetime import timedelta, datetime

h, m, s = input().split(':')
time = datetime(1, 1, 1, int(h), int(m), int(s)) + timedelta(seconds=int(input()))
print(time.time())