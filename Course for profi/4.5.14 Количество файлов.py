from zipfile import ZipFile, ZipInfo

with ZipFile('workbook.zip') as zippy:
    count = 0
    for file in zippy.infolist():
        if not file.is_dir():
            count += 1
print(count)