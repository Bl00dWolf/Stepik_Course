from collections import Counter

counts = Counter()
for line in open(0):
    counts[line.strip()] += 1
print(counts.total() - len(counts))

# еще вариант
# print(len(cards := [x.rstrip() for x in open(0)]) - len(set(cards)))