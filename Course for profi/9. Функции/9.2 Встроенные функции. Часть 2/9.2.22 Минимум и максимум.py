funcc = input()
a, b = (int(num) for num in input().split())

answers = [eval(funcc) for x in range(a, b+1)]
print(f'Минимальное значение функции {funcc} на отрезке [{a}; {b}] равно {min(answers)}')
print(f'Максимальное значение функции {funcc} на отрезке [{a}; {b}] равно {max(answers)}')