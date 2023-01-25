from zipfile import ZipFile, ZipInfo


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zippy:
        if args:
            for file in args:
                zippy.extract(file)
        else:
            zippy.extractall()


extract_this('workbook.zip', 'earth.jpg', 'exam.txt')

# еще вариант
# from zipfile import ZipFile
#
#
# def extract_this(zip_name: str, *args):
#     if not args:
#         args = None
#     with ZipFile(zip_name) as zf:
#         zf.extractall(members=args)