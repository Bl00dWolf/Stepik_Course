from collections import Counter

[print(f'{k}: {v}') for k, v in sorted(Counter([word for word in input().split(',')]).items())]