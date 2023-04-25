def get_all_values(data, key):
    keys_set = set()
    if key in data:
        keys_set.add(data[key])

    for k, v in data.items():
        if type(v) == dict:
            value = get_all_values(v, key)  # рекурсивный случай
            keys_set.update(value)
    return keys_set