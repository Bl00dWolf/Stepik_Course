from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.__aliases = {}
        self.list_alis = []
        super().__init__(*args, **kwargs)

    def alias(self, orig_key, alis):
        if alis in self.list_alis:
            for key_mapping in self.__aliases.values():
                if alis in key_mapping[0]:
                    del key_mapping[0][key_mapping[0].index(alis)]
        if orig_key not in self.__aliases:
            self.__aliases[orig_key] = [[alis], self.data[orig_key]]
            self.list_alis.append(alis)
        elif orig_key in self.__aliases:
            self.__aliases[orig_key][0].append(alis)
            self.list_alis.append(alis)
        print(self.__aliases)
        print(list(self.__aliases.values()))

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]
        for key_mapping in self.__aliases.values():
            if item in key_mapping[0]:
                return key_mapping[1]
        raise KeyError

    def __setitem__(self, key, value):
        for key_orig, key_mapping in self.__aliases.items():
            if key in key_mapping[0] or key in self.__aliases.keys():
                key_mapping[1] = value
                self.data[key_orig] = value
                return None
        self.data[key] = value


mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['x'] += 1
print(mkey['x'], mkey['y'], mkey['z'])
