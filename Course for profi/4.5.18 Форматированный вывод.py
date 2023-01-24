from zipfile import ZipFile, ZipInfo
from datetime import datetime

with ZipFile('workbook.zip') as zippy:
    for file in sorted(zippy.infolist(), key=lambda x: x.filename.rsplit('/', maxsplit=1)[-1]):
        if not file.is_dir():
            print(file.filename.rsplit('/', maxsplit=1)[-1])
            print(f'  Дата модификации файла: {datetime(*file.date_time)}')
            print(f'  Объем исходного файла: {file.file_size} байт(а)')
            print(f'  Объем сжатого файла: {file.compress_size} байт(а)\n')