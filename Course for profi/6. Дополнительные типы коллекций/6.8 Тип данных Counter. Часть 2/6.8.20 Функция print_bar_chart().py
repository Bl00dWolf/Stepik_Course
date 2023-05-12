from collections import Counter

def print_bar_chart(data: str | list[str], mark: str):
    counts = Counter()
    for line in data:
        counts[line] += 1
    offset = len(max(counts.keys(), key=len))

    for k, v in counts.most_common():
        print(f'{k.ljust(offset)} |{mark * v}')
