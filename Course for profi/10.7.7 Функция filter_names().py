def filter_names(names: list, ignore_char: str, max_names: int):
    filt_char = (name for name in names if name[0].lower() != ignore_char.lower())
    filt_num = (name for name in filt_char if name.isalpha())
    filt_max = (i for i in range(max_names))
    return (name for indx, name in zip(filt_max, filt_num))


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))
