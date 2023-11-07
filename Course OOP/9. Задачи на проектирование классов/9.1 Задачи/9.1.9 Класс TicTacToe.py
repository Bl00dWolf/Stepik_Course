class TicTacToe:
    def __init__(self):
        self.gamefield = [[' ', ' ', ' '] for _ in range(3)]
        self.player = 'X'
        self.moves_count = 0

    def _iswinner_(self):
        gm = self.gamefield
        for symbol in 'XO':
            # строки
            if symbol in gm[0][0] and symbol in gm[0][1] and symbol in gm[0][2]:
                return symbol
            elif symbol in gm[1][0] and symbol in gm[1][1] and symbol in gm[1][2]:
                return symbol
            elif symbol in gm[2][0] and symbol in gm[2][1] and symbol in gm[2][2]:
                return symbol

            # столбцы
            elif symbol in gm[0][0] and symbol in gm[1][0] and symbol in gm[2][0]:
                return symbol
            elif symbol in gm[0][1] and symbol in gm[1][1] and symbol in gm[2][1]:
                return symbol
            elif symbol in gm[0][2] and symbol in gm[1][2] and symbol in gm[2][2]:
                return symbol

            # диагонали
            elif symbol in gm[0][0] and symbol in gm[1][1] and symbol in gm[2][2]:
                return symbol
            elif symbol in gm[0][2] and symbol in gm[1][1] and symbol in gm[2][0]:
                return symbol
        return 'NO_WINNER_YET'

    def mark(self, x: int, y: int):
        if self._iswinner_() in 'XO' or self._iswinner_() == 'NO_WINNER_YET' and self.moves_count == 9:
            print('Игра окончена')
        elif self.gamefield[x - 1][y - 1] in 'XO':
            print('Недоступная клетка')
        elif self.player == 'X':
            self.gamefield[x - 1][y - 1] = 'X'
            self.player = 'O'
            self.moves_count += 1
        elif self.player == 'O':
            self.gamefield[x - 1][y - 1] = 'O'
            self.player = 'X'
            self.moves_count += 1

    def winner(self):
        curwin = self._iswinner_()
        if self.moves_count == 9 and curwin == 'NO_WINNER_YET':
            return 'Ничья'
        elif curwin == 'NO_WINNER_YET':
            return None
        elif curwin in 'XO':
            return curwin

    def show(self):
        for i in range(len(self.gamefield)):
            for j in range(len(self.gamefield[i])):
                print(f'{self.gamefield[i][j]}' if j == len(self.gamefield[i]) - 1 else f'{self.gamefield[i][j]}|',
                      end='')
            print('\n-----' if i != len(self.gamefield) - 1 else '')


# еще вариант
# class TicTacToe:
#
#     def __init__(self):
#         self.board = [[' ', ' ', ' '],
#                       [' ', ' ', ' '],
#                       [' ', ' ', ' ']]
#         self.flag = True
#
#     def mark(self, x, y):
#         if self.winner() is not None:
#             print('Игра окончена')
#         elif self.board[x-1][y-1] == ' ':
#             self.board[x-1][y-1] = ['O', 'X'][self.flag]
#             self.flag = not self.flag
#         else:
#             print('Недоступная клетка')
#
#     def show(self):
#         print(*self.board[0], sep='|')
#         print('-----')
#         print(*self.board[1], sep='|')
#         print('-----')
#         print(*self.board[2], sep='|')
#
#     def winner(self):
#
#         for line in self.board:
#             if ''.join(line) == 'XXX':
#                 return 'X'
#             if ''.join(line) == 'OOO':
#                 return 'O'
#
#         for line in zip(*self.board):
#             if ''.join(line) == 'XXX':
#                 return 'X'
#             if ''.join(line) == 'OOO':
#                 return 'O'
#
#         s1 = s2 = ''
#         for i in range(3):
#             s1 += self.board[i][i]
#             s2 += self.board[i][~i]
#         if s1 == 'XXX' or s2 == 'XXX':
#             return 'X'
#         if s1 == 'OOO' or s2 == 'OOO':
#             return 'O'
#
#         if ' ' not in sum(self.board, []):
#             return 'Ничья'