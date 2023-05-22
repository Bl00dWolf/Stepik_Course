class Bee:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move_up(self, n: int):
        self.y += n

    def move_down(self, n: int):
        self.y -= n

    def move_right(self, n: int):
        self.x += n

    def move_left(self, n: int):
        self.x -= n
