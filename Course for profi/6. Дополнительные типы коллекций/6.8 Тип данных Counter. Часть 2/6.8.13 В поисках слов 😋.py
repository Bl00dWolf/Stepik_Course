from collections import Counter

counts = Counter(input().lower().split()).most_common()
counts = list(sorted(filter(lambda x: x[1] == counts[-1][1], counts), key=lambda x: x[0]))

s = ''
for obj, num in counts:
    s += obj + ', '
print(s[:-2])

