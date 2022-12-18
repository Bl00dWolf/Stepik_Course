from datetime import timedelta

s = input().split(':')
print(int(timedelta(hours=int(s[0]), minutes=int(s[1]), seconds=int(s[2])).total_seconds()))

# Еще вариант решения
# from datetime import datetime, timedelta
#
# h, m, s = map(int, input().split(':'))
#
# td = timedelta(hours=h, minutes=m, seconds=s)
#
# print(int(td.total_seconds()))