import re

data = input()
pattern = r'^(Здравствуйте|Доброе утро|Добрый день|Добрый вечер)'
if re.search(pattern, data, flags=re.IGNORECASE):
    print('True')
else:
    print('False')