class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return True
