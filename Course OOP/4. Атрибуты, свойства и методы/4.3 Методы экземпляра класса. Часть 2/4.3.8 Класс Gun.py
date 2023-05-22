class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        if self.count % 2 == 0:
            print('pif')
        else:
            print('paf')

        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0
