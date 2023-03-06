def hash_as_key(objects: list) -> dict:
    nwbjs = dict()
    for object in objects:
        if hash(object) not in nwbjs:
            nwbjs[hash(object)] = object
        elif not isinstance(nwbjs[hash(object)], list):
            nwbjs[hash(object)] = [nwbjs[hash(object)]]
            nwbjs[hash(object)].extend([object])
        else:
            nwbjs[hash(object)].extend([object])
    return nwbjs


# еще вариант
# def hash_as_key(objects):
#     rv = {}
#     for i in objects:
#         rv.setdefault(hash(i), []).append(i)
#     return {i: j if len(j) > 1 else j[0] for i, j in rv.items()}
