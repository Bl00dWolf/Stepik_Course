from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()
    return chainmap.get(key)
