# def traffic(n):
#     while n > 0:
#         print('Не парковаться')
#         n -= 1

def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)
