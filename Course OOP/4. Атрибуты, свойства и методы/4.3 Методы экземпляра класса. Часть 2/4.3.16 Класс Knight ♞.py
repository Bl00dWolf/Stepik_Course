class Knight:
    hor_pos = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal, self.vertical = horizontal, vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, x: str, y: int):
        if (Knight.hor_pos[self.horizontal] - Knight.hor_pos[x]) ** 2 + (self.vertical - y) ** 2 == 5:
            return True
        return False

    def move_to(self, x: str, y: int):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        board = [[' . '] * 8 for _ in range(8)]
        board[Knight.hor_pos[self.horizontal] - 1][self.vertical - 1] = ' N '
        hor_pos_int = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

        for i in range(7, -1, -1):
            for j in range(8):
                if self.can_move(hor_pos_int[j + 1], i + 1):
                    board[j][i] = ' * '
                print(board[j][i], sep='', end='')
            print()
