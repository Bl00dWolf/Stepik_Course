import sys


class UpperPrint:
    def __enter__(self):
        self.standard_output = sys.stdout
        self.file = open('temp.txt', 'w+', encoding='UTF-8')
        sys.stdout = self.file

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.standard_output
        self.file.seek(0, 0)
        [print(line.upper(), end='', sep='') for line in self.file.readlines()]
        self.file.close()

# еще вариант
# import sys
#
#
# class UpperPrint:
#     def __enter__(self):
#         self.original_write = sys.stdout.write
#         sys.stdout.write = self.upper_write
#         return self
#
#     def upper_write(self, text):
#         self.original_write(text.upper())
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         sys.stdout.write = self.original_write

# import sys
#
# class UpperPrint:
#     def __enter__(self):
#         self.w = sys.stdout.write
#         sys.stdout.write = lambda t: self.w(t.upper())
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout.write = self.w
