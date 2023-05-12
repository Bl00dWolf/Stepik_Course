import re
import sys

data = [line.strip() for line in sys.stdin]

for line in data:
    match1 = re.search(r'\b(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})\b', line)
    if match1:
        print(f'Код страны: {match1.group(1)}, Код города: {match1.group(3)}, Номер: {match1.group(4)}')