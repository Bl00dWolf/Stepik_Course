class WriteSpy:
    def __init__(self, file1, file2, to_close: bool = False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()

    def write(self, text: str):
        if self.file1.closed or self.file2.closed or not self.file1.writable() or not self.file2.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        return self.file1.writable() and self.file2.writable()

    def closed(self):
        return self.file1.closed and self.file2.closed
