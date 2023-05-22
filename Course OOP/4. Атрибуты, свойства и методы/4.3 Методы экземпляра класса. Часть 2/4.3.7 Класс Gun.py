class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        if self.count == 0:
            print('pif')
            self.count = 1
        elif self.count == 1:
            print('paf')
            self.count = 0
