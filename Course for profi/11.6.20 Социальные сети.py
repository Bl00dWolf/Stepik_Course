import re
import sys

data = [line.strip() for line in sys.stdin]

count = 0
for line in data:
    if re.search(r'beegeek', line, re.I):
        count += 1
print(count)