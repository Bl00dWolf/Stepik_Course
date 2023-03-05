def get_all_values(data, key):
    keys_set = set()
    if key in data:
        keys_set.add(data[key])
        return keys_set  # базовый случай

    for k, v in data.items():
        if type(v) == dict:
            value = get_all_values(v, key)  # рекурсивный случай
            keys_set.update(value)
            return keys_set
            # if value is not None:
            #     return value


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
