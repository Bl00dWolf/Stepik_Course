from collections import defaultdict


def flip_dict(dict_of_lists: dict) -> defaultdict:
    ddict = defaultdict(list)
    for key, listek in dict_of_lists.items():
        for num in listek:
            ddict[num].append(key)
    return ddict


# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
