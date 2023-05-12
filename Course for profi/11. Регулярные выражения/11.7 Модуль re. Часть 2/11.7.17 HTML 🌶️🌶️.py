import re

res = {}
for line in open(0):
    for tag, params in re.findall(r'<(\w+)(.*?)>', line):
        res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))

for key in sorted(res):
    print(f'{key}: {", ".join(sorted(res[key]))}')