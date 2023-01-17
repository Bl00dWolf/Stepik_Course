import json
import sys

s = sys.stdin.read()
s = json.loads(s)
for k, v in s.items():
    if type(v) == list:
        v = map(str, v)
        print(f'{k}: {", ".join(v)}')
    else:
        print(f'{k}: {v}')

# Чуть более изящное решение
# import sys
# import json
#
# data = json.loads(sys.stdin.read())
#
# for key, value in data.items():
#     if isinstance(value, list):
#         print(f'{key}: {", ".join(map(str, value))}')
#     else:
#         print(f'{key}: {value}')
