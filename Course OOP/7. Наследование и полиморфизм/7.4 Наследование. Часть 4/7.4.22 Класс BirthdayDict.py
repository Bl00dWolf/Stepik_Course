from collections import UserDict


class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        super().__setitem__(key, value)
