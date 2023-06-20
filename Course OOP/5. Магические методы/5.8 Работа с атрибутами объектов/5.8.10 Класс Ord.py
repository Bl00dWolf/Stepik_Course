class Ord:
    def __getattr__(self, item):
        return ord(item)
