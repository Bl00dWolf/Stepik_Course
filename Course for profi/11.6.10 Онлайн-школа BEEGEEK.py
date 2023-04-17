import re
import sys

data = [line.strip() for line in sys.stdin]

for line in data:
    match = re.search(r'^_\d+[a-zA-Z]*_?$', line)
    if match:
        print('True')
    else:
        print('False')
