def power(degree: int):
    def powishe(x):
        return x ** degree

    return powishe


# square = power(2)
# print(square(5))

# еще вариант
# power = lambda degree: (lambda num: pow(num, degree))