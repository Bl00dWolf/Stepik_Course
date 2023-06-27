import random


class RandomLooper:
    def __init__(self, *args):
        self.objs = []
        for ls in args:
            self.objs.extend(ls)
        random.shuffle(self.objs)
        self.objs = iter(self.objs)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.objs)
