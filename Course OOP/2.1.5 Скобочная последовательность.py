import re

# Неверный паттерн, пока не знаю как сделать верно это задание
if re.fullmatch(r'\(.*?\)', input()):
    print('True')
else:
    print('False')