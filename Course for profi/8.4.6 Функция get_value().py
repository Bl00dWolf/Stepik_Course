def get_value(data, key):
    if key in data:
        return data[key]  # базовый случай

    for k, v in data.items():
        if type(v) == dict:
            value = get_value(v, key)  # рекурсивный случай
            if value is not None:
                return value