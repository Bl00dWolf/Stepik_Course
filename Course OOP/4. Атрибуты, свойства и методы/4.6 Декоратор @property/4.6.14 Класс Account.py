def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10 ** 9


class Account:
    def __init__(self, login: str, password: str):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, value):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd: str):
        self._password = hash_function(passwd)
