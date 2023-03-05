def dict_travel(data, path=''):

    for k, v in sorted(data.items()):
        if type(v) == dict:
            dict_travel(v, path + '.' + k)
        else:
            print(f"{(path + '.' + k)[1:]}: {v}")