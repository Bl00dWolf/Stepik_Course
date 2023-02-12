from collections import Counter

counts = Counter([len(word) for word in input().split()])
[print(f'Слов длины {gp_words}: {num}') for gp_words, num in sorted(counts.items(), key=lambda x: x[1])]