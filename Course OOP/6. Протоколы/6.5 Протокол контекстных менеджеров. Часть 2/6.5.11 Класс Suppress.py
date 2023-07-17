class Suppress:
    def __init__(self, *args):
        self._exc = list(args)

    def __enter__(self):
        self.exception = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self._exc:
            self.exception = exc_val
            return True
        return False
