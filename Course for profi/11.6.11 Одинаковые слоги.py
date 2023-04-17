import re
import sys

data = [line.strip() for line in sys.stdin]

for line in data:
    match = re.search(r'^(\w+)\1$', line)
    if match:
        print(line)
