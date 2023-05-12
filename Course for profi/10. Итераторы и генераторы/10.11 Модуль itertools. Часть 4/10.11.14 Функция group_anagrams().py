from itertools import groupby


def group_anagrams(words: list[str]) -> list[tuple]:
    listek = []
    gp = groupby(sorted(words, key=lambda x: sorted(x)), key=lambda x: sorted(x))
    for priznak, words in gp:
        listek.append(tuple(words))
    return listek


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)
