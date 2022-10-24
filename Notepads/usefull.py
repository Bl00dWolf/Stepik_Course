# Печатает матрицу
def print_matrix(matrix, reverse=False):
    '''
    :param matrix: Сама матрица
    :param reverse: если true то печатает матрицу как колонка, столбец
    :return: None
    '''
    print("-" * 15)
    if not reverse:
        for row in matrix:
            print(*row)
    if reverse:
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                print(matrix[r][c], end=' ')
            print()


# удобные наброски для текущих задач
n = int(input())
matrix = [input().split() for _ in range(n)]

n = 3
matrix = [['0', '1', '2'],
          ['1', '2', '7'],
          ['2', '3', '4']]
