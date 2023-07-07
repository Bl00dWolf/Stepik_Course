from datetime import datetime, date


def log_for(logfile: str, date_str: str):
    with (open(logfile, 'r', encoding='UTF-8') as f_inp,
          open(f'log_for_{date_str}.txt', 'w', encoding='UTF-8') as f_out):
        correct = filter(
            lambda x: datetime.strptime(x.strip().split(' ', 1)[0], '%Y-%m-%d') == datetime.strptime(date_str,
                                                                                                     '%Y-%m-%d'),
            f_inp.readlines())

        for line in correct:
            line = line.split(maxsplit=1)[1:]
            f_out.write(' '.join(line))

# еще вариант
# def log_for(logfile, date_str):
#     with open(f'log_for_{date_str}.txt', 'w') as result:
#         for line in open(logfile):
#             if date_str in line:
#                 date, info = line.split(' ', 1)
#                 result.write(info)
