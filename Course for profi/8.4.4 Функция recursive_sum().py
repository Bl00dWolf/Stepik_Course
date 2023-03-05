def recursive_sum(nested_lists: list, summ=0) -> int:
    if isinstance(nested_lists, int):
        summ += nested_lists
    if isinstance(nested_lists, list):
        for i in nested_lists:
            summ += recursive_sum(i)
    return summ

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
