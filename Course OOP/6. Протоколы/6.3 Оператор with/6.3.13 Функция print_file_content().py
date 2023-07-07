def print_file_content(filename: str):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            print(*file.readlines(), end='', sep='')
    except FileNotFoundError:
        print('Файл не найден')