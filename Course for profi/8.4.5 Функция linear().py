def linear(li):
    new_list = []
    for elem in li:
        if isinstance(elem, list):
            new_list.extend(linear(elem))
        else:
            new_list.append(elem)
    return new_list

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(linear(my_list))