class Alphabet:
    def __init__(self, language):
        self.alpha = {'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 'en': 'abcdefghijklmnopqrstuvwxyz'}
        self.language = language
        self.iiter = iter(self.alpha[self.language])

    def __iter__(self):
        return self

    def __next__(self):
        cur_alp = next(self.iiter, None)
        if cur_alp is not None:
            return cur_alp
        self.iiter = iter(self.alpha[self.language])
        return next(self.iiter)
