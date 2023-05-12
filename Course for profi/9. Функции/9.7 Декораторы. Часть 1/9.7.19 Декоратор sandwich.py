def sandwich(func):
    def wrapper(*args, **kwargs):
        up, down = '---- Верхний ломтик хлеба ----', '---- Нижний ломтик хлеба ----'
        print(up)
        result = func(*args, **kwargs)
        print(down)
        return result

    return wrapper


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())
