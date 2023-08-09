from contextlib import contextmanager


@contextmanager
def safe_write(filename: str):
    try:
        file = open(filename, 'w', encoding='utf-8')
        yield file
        file.close()
    except Exception as err:
        print(f'Во время записи в файл было возбуждено исключение {type(err).__name__}')
        file.close()


with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('undertale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('undertale.txt') as file:
    print(file.read())