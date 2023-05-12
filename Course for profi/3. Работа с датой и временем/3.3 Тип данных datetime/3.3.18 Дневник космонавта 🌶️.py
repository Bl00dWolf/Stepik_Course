from datetime import datetime

with open('diary.txt', encoding='UTF-8') as diary:
    s = diary.read().split('\n\n')

s = [stroka.split('\n', 1) for stroka in s]
notes = {datetime.strptime(k, '%d.%m.%Y; %H:%M'): v for k, v in s}

for tdata, note in sorted(notes.items()):
    print(f'{tdata.strftime("%d.%m.%Y; %H:%M")}\n{note}\n')

# Понравилось еще это роешение
# with open('diary.txt', encoding="utf-8") as f1:
#
#     print(*sorted(f1.read().split('\n\n'),
#                   key=lambda t: datetime.strptime(t.split('\n')[0], '%d.%m.%Y; %H:%M')), sep='\n\n')