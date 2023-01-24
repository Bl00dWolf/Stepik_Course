from zipfile import ZipFile, ZipInfo

with ZipFile('workbook.zip') as zippy:
    sum_compressed_size, sum_orig_size = 0, 0
    for file in zippy.infolist():
        sum_orig_size += file.file_size
        sum_compressed_size += file.compress_size
print(f'Объем исходных файлов: {sum_orig_size} байт(а)\nОбъем сжатых файлов: {sum_compressed_size} байт(а)')

# еще решение
# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     print(f'Объем исходных файлов: {sum(f.file_size for f in info)} байт(а)')
#     print(f'Объем сжатых файлов: {sum(f.compress_size for f in info)} байт(а)')


