from contextlib import contextmanager


@contextmanager
def safe_write(filename: str):
    try:
        try:
            file = open(filename, 'rb')
            data = file.read()
            file.close()
        except:
            pass
        file = open(filename, 'w', encoding='utf-8')
        yield file
        file.close()
    except Exception as err:
        print(f'Во время записи в файл было возбуждено исключение {type(err).__name__}')
        file.close()
        file = open(filename, 'wb')
        file.write(data)
