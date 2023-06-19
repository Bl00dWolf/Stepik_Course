class Calculator:
    def __call__(self, a: int | float, b: int | float, operation: str):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '/':
            if b == 0:
                raise ValueError('Деление на ноль невозможно')
            return a / b
        elif operation == '*':
            return a * b

# еще 2 варианта
# class Calculator:
#     def __call__(self, a, b, operation):
#         match operation:
#             case '+':
#                 return a + b
#             case '-':
#                 return a - b
#             case '*':
#                 return a * b
#             case '/':
#                 if b == 0:
#                     raise ValueError('Деление на ноль невозможно')
#                 return a / b
#
# class Calculator:
#     def __call__(self, a, b, operation):
#         if operation == '/' and b == 0:
#             raise ValueError('Деление на ноль невозможно')
#         return eval(f'{a}{operation}{b}')