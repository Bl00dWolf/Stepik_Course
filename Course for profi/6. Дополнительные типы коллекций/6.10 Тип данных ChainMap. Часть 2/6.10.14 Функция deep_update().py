from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value) -> None:
    flag = False
    for dict in chainmap.maps:
        if key in dict:
            flag = True
            dict[key] = value
    if not flag:
        chainmap[key] = value

# еще вариант
# def deep_update(chainmap, key, value):
#     if key in chainmap:
#         [dct.update({key: value}) for dct in chainmap.maps if key in dct]
#     else:
#         chainmap[key] = value