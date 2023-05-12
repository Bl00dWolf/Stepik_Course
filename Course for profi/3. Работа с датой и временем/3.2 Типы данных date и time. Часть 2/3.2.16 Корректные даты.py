from datetime import date


def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return True
    except:
        return False


count = 0
while True:
    s = input()
    if s == 'end':
        break
    if is_correct(*s.split('.')):
        print('Корректная')
        count += 1
    else:
        print('Некорректная')
print(count)
