from collections import ChainMap


def get_all_values(chainmap: ChainMap, key) -> set:
    kset = set()
    for ddict in chainmap.maps:
        if ddict.get(key):
            kset.add(ddict.get(key))
    return kset

# еще вариант
# def get_all_values(chainmap, key):
#     return {d[key] for d in chainmap.maps if key in d}