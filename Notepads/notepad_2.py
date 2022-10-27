matrix_1 = [[1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]]

matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


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


for row in matrix_multiply(matrix_1, matrix_2):
    print(*row)
