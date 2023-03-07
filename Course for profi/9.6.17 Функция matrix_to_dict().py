def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    dict = {}
    for i, list in enumerate(matrix, 1):
        dict[i] = list
    return dict

# еще вариант
# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
#     return dict(enumerate(matrix, 1))