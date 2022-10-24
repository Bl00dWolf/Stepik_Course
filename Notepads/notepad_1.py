horse_pos = input().lower()
chess = []
abc_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

[chess.append(['.'] * 8) for _ in range(8)]


def print_matrix(matrix, reverse=False):
    '''
    :param matrix: Сама матрица
    :param reverse: если true то печатает матрицу как колонка, столбец
    :return: None
    '''
    if not reverse:
        for row in matrix:
            print(*row)
    if reverse:
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                print(matrix[r][c], end=' ')
            print()


horse_x = 7 - (int(horse_pos[1]) - 1)
horse_y = abc_input.index(horse_pos[0])
chess[horse_x][horse_y] = 'N'

for i in range(8):
    for j in range(8):
        if abs((horse_x - j) * (horse_y - i)) == 2:
            chess[j][i] = '*'

print_matrix(chess)
