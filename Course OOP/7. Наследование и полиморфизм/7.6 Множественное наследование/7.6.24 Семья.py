class Human:
    _greet_phrase_ = ''

    def __init__(self, mood: str = 'neutral'):
        self.mood = mood

    @classmethod
    def greet(cls):
        return cls._greet_phrase_


class Father(Human):
    _greet_phrase_ = 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Human):
    _greet_phrase_ = 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass
