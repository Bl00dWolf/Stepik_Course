import random


class Cell:
    def __init__(self, row: int, col: int):
        self.open = False
        self.mine = False
        self.neighbours = 0
        self.row = row
        self.col = col


class Game:

    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self._mines_count = 0

        # Создаем и заполняем доску клетками
        self.board = [[Cell(i, j) for j in range(self.cols)] for i in range(self.rows)]

        # Выбираем координаты мин, но в одномерном листе
        mines_coords_list = random.sample(range(self.cols * self.rows), self.mines)
        # Переводим эти координаты в матрицу обратно
        mines_coords_matrix = [(num // self.cols, num % self.cols) for num in mines_coords_list]
        # Выставляем мины по этим координатам
        for i, j in mines_coords_matrix:
            self.board[i][j].mine = True

        # Выставляем атрибут соседей у каждой клетки
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                neighbours = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
                for nb_cell_i, nb_cell_j in neighbours:
                    if 0 <= i + nb_cell_i < len(self.board) and 0 <= j + nb_cell_j < len(self.board[i]) and \
                            self.board[i + nb_cell_i][j + nb_cell_j].mine:
                        self.board[i][j].neighbours += 1
