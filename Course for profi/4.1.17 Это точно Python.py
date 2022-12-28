import sys
from datetime import date, datetime

dates = [datetime.strptime(d.strip(), '%d.%m.%Y').date() for d in sys.stdin.readlines()]

dnum = []
[dnum.append(dates[i + 1].toordinal() - dates[i].toordinal()) for i in range(len(dates) - 1)]

if len(list(filter(lambda x: x > 0, dnum))) == len(dnum):
    print('ASC')
elif len(list(filter(lambda x: x < 0, dnum))) == len(dnum):
    print('DESC')
else:
    print('MIX')

# Еще решение
# import sys
# from datetime import datetime
#
# data = [datetime.strptime(d.rstrip(), '%d.%m.%Y') for d in sys.stdin]
# s_data = sorted(set(data))
# print(('ASC', 'DESC', 'MIX')[(s_data, s_data[::-1], data).index(data)])