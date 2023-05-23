class User:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Некорректное имя')
        if not isinstance(age, int) or not (0 <= age <= 110):
            raise ValueError('Некорректный возраст')

        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, new_name: str):
        if not isinstance(new_name, str) or not new_name.isalpha():
            raise ValueError('Некорректное имя')
        self._name = new_name

    def set_age(self, new_age: int):
        if not isinstance(new_age, int) or not (0 <= new_age <= 110):
            raise ValueError('Некорректный возраст')
        self._age = new_age

# еще вариант:
# class User:
#     def __init__(self, name, age):
#         self.set_name(name)
#         self.set_age(age)
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, new_name):
#         if not (isinstance(new_name, str) and new_name.isalpha() and new_name):
#             raise ValueError('Некорректное имя')
#         self._name = new_name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, new_age):
#         if not (isinstance(new_age, int) and (0 <= new_age <= 110)):
#             raise ValueError('Некорректный возраст')
#         self._age = new_age
