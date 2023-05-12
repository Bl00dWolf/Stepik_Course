from zipfile import ZipFile, ZipInfo

with ZipFile('workbook.zip') as zippy:
    max_eff = min((file.compress_size / file.file_size, file.filename) for file in zippy.infolist() if
                  file.compress_size != 0 and file.file_size != 0)
    print(max_eff[1].split('/')[-1])

# еще вариант
# from zipfile import ZipFile
#
# with ZipFile("workbook.zip") as zip_file:
#     filelist = zip_file.infolist()
#     t = ((f.filename, f.compress_size/f.file_size) for f in filelist
#          if f.file_size != 0)
#     print(min(t, key=lambda x: x[1])[0].split("/")[-1])