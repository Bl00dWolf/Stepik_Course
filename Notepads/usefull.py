# Печатает матрицу
def print_matrix(matrix, reverse=False):
    """
    :param matrix: Сама матрица
    :param reverse: если true то печатает матрицу как колонка, столбец
    :return: None
    """
    if not reverse:
        for row in matrix:
            print(*row)
    if reverse:
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                print(matrix[r][c], end=' ')
            print()


# Умножение двух матриц:
def matrix_multiply(matrix_1, matrix_2):
    """
    Возвращает матрицу - результат перемножения двух переданных матриц.
    Число строк и столбцов должно быть одинаковым!
    :param matrix_1: Первая матрица
    :param matrix_2: Вторая матрица
    :return: Матрица - результат перемножения
    """
    matrix_3 = [[0] * len(row) for row in matrix_1]

    for k in range(len(matrix_3[0])):
        for i in range(len(matrix_3)):
            for j in range(len(matrix_3[i])):
                matrix_3[i][j] += matrix_1[i][j] * matrix_2[k][j]
    return matrix_3


# удобные наброски для текущих задач
n = int(input())
matrix = [input().split() for _ in range(n)]

n = 3
matrix = [['0', '1', '2'],
          ['1', '2', '7'],
          ['2', '3', '4']]
