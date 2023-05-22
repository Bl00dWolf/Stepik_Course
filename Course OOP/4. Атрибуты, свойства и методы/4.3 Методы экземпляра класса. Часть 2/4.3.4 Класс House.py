class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color: str):
        self.color = new_color

    def add_rooms(self, n: int):
        self.rooms += n
