from collections import Counter
import sys

counts = Counter()
for line in sys.stdin.readlines():
    name, mark = line.strip().split()
    counts[name] = int(mark)

print(counts.most_common()[-2][0])

