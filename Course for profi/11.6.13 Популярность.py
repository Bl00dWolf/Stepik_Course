import re
import sys

data = [line.strip() for line in sys.stdin]

pattern1 = r'^(beegeek).*\1$'  # начинается и заканчивается, 3 балла
pattern2 = r'^(beegeek).*|.*(beegeek)$'  # только начинается или только заканчивается, 2 балла
pattern3 = r'beegeek'

score = 0
for line in data:
    if re.search(pattern1, line):
        score += 3
    elif re.search(pattern2, line):
        score += 2
    elif re.search(pattern3, line):
        score += 1

print(score)
