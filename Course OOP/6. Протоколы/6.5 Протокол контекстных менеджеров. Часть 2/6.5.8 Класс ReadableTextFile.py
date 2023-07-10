class ReadableTextFile:
    def __init__(self, filename: str):
        self._filename = filename

    def __enter__(self):
        with open(self._filename, 'r', encoding='UTF-8') as fl:
            data = map(str.strip, fl.readlines())
        return data

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

# еще вариант
#
#
# class ReadableTextFile:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         self.obj = open(self.filename, 'r', encoding='utf-8')
#         return (line.strip() for line in self.obj)
#
#     def __exit__(self, *args, **kwargs):
#         self.obj.close()