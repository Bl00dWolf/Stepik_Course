class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def _create_matrix_instance(self, rows, cols, sign=1, do_transpose=False, do_round=False, n=None):
        matrix = Matrix(rows, cols)
        for row in range(rows):
            for col in range(cols):
                r, c = (col, row) * do_transpose or (row, col)
                value = round(self.get_value(r, c) * sign, n) * do_round or self.get_value(r, c) * sign
                matrix.set_value(row, col, value)
        return matrix

    def __str__(self):
        string_matrix = [' '.join(map(str, item)) for item in self.matrix]
        return '\n'.join(string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        return self._create_matrix_instance(self.rows, self.cols)

    def __neg__(self):
        return self._create_matrix_instance(self.rows, self.cols, sign=-1)

    def __invert__(self):
        return self._create_matrix_instance(self.cols, self.rows, do_transpose=True)

    def __round__(self, n=None):
        return self._create_matrix_instance(self.rows, self.cols, do_round=True, n=n)
