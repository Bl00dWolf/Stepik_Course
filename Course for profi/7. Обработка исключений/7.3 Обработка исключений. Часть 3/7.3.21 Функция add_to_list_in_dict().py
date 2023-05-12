# def add_to_list_in_dict(data: dict, key, element) -> None:
#     data.setdefault(key, []).append(element)

def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except KeyError:
        data[key] = [element]