from collections import Counter

print(Counter([word.lower() for word in input().split()]).most_common()[0][0])
