class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + ' ' + self.surname

    def set_fullname(self, fullname: str):
        name, surname = fullname.split()
        self.name = name
        self.surname = surname

    fullname = property(get_fullname, set_fullname)


person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)
