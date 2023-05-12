from collections import Counter

print(sorted(Counter(input().lower().split()).most_common(), key=lambda x: (x[1], x[0]), reverse=True)[0][0])