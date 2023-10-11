from collections.abc import Sequence


class DNA(Sequence):
    __seq = {
        "T": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }

    def __init__(self, chain: str):
        self._chain_ = chain

    def __getitem__(self, item):
        if isinstance(item, int | slice):
            return self._chain_[item], self.__class__.__seq[self._chain_[item]]
        return NotImplemented

    def __len__(self):
        return len(self._chain_)

    def __str__(self):
        return self._chain_

    def __contains__(self, item):
        return item in self._chain_

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self._chain_ + other._chain_)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._chain_ == other._chain_
        return NotImplemented
