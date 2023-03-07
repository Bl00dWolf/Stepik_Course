# def generator_square_polynom(a: int, b: int, c: int):
#     def refunc(x):
#         return a * x ** 2 + b * x + c
#
#     return refunc


generator_square_polynom = lambda a, b, c: lambda x: a * x ** 2 + b * x + c

# f = generator_square_polynom(1, 2, 1)
# print(f(5))
