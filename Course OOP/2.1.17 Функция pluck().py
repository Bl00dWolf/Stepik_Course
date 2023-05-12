def pluck(data: dict, path: str, default=None):
    kkeys = path.split('.')
    if len(kkeys) == 1:
        return data.get(kkeys[0], default)
    else:
        if isinstance(data[kkeys[0]], dict):
            return pluck(data[kkeys.pop(0)], '.'.join(kkeys), default)
        else:
            return default

# еще вариант:
# def pluck(data, path, default=None):
#     for key in path.split('.'):
#         data = data.get(key, default)
#     return data