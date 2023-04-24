import re
import sys

data = sys.stdin.read()
res = re.findall(r'<a href=\"(.+)\">(.+)</a>', data)

for link, text in res:
    print(f'{link}, {text}')