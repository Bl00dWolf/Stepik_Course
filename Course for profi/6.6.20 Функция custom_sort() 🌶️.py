from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    if by_values:
        for key in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)
