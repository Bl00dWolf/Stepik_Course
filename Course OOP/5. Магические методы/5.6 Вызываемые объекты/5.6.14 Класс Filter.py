class Filter:
    def __init__(self, predicate):
        if predicate is None:
            predicate = bool
        self.predicate = predicate

    def __call__(self, iterable):
        return [*filter(self.predicate, iterable)]
