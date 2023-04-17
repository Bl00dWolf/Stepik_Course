import re
import sys

data = [line.strip() for line in sys.stdin]

bee, geek = 0, 0
for line in data:
    match1 = re.search(r'(bee).*\1', line)
    match2 = re.search(r'\bgeek\b', line)
    if match1:
        bee += 1
    if match2:
        geek += 1

print(f'{bee}\n{geek}')
