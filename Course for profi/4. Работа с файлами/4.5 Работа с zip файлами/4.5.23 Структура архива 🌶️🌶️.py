from zipfile import ZipFile


def size_of(size: int) -> str:
    if 0 < size < 1024:
        return str(size) + ' B'
    elif 1024 <= size <= 1024 ** 2:
        return str(round(size / 1024)) + ' KB'
    elif 1024 ** 2 <= size <= 1024 ** 3:
        return str(round(size / 1024 ** 2)) + ' MB'
    elif 1024 ** 3 <= size <= 1024 ** 4:
        return str(round(size / 1024 ** 3)) + ' GB'


with ZipFile('desktop.zip') as zippy:
    for file in zippy.infolist():
        if not file.is_dir():
            slashes = (file.filename.count('/') - 1) * 2 + 2
            print(f'{" " * slashes}{file.filename.rsplit("/", maxsplit=1)[-1]} {size_of(file.file_size)}')
        else:
            slashes = (file.filename.count('/') - 1) * 2
            print(f'{" " * slashes}{file.filename.rsplit("/", maxsplit=2)[-2]}')
