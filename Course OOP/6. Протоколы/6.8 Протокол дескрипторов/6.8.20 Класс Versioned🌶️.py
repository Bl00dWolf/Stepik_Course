class Versioned:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

        if 'cache' in instance.__dict__:
            instance.__dict__['cache'].append(value)
        else:
            instance.__dict__['cache'] = []
            instance.__dict__['cache'].append(value)

    def get_version(self, instance, n: int):
        # print('get ', instance.cache)
        return instance.cache[n - 1]

    def set_version(self, instance, n: int):
        # print('set ', instance.cache)
        instance.__dict__[self._name] = instance.cache[n - 1]


# еще вариант
#
#
# class Versioned:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self.name not in instance.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return instance.__dict__[self.name][-1]
#
#     def __set__(self, instance, value):
#         instance.__dict__.setdefault(self.name, []).append(value)
#
#     def get_version(self, instance, n):
#         return instance.__dict__[self.name][n - 1]
#
#     def set_version(self, instance, n):
#         instance.__dict__[self.name].append(self.get_version(instance, n))

