class Reloopable:
    def __init__(self, file):
        self._file = file

    def __enter__(self):
        return self._file.readlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
