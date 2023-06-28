class ReversedSequence:
    def __init__(self, sequence):
        self._seq = sequence

    def __len__(self):
        return len(self._seq)

    def __iter__(self):
        yield from self._seq[::-1]

    def __getitem__(self, item):
        item += 1
        return self._seq[-item]
