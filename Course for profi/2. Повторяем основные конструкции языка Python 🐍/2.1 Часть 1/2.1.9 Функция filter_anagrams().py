from functools import reduce


def filter_anagrams(word, words):
    listek = []

    # word_weight = sum(map(lambda x: ord(x), word))
    word_weight = reduce(lambda a, b: a + ord(b), word, 0)
    [listek.append(word_in_list) for word_in_list in words if reduce(lambda a, b: a + ord(b), word_in_list, 0) == word_weight]

    return listek