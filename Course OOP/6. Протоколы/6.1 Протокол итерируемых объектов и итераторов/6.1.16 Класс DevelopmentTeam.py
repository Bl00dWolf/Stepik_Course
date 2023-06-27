class DevelopmentTeam:
    def __init__(self):
        self._devs_jun = []
        self._devs_sen = []

    def add_junior(self, *args):
        for dev in args:
            self._devs_jun.append((dev, 'junior'))

    def add_senior(self, *args):
        for dev in args:
            self._devs_sen.append((dev, 'senior'))

    def __iter__(self):
        yield from self._devs_jun + self._devs_sen
