class CardDeck:
    def __init__(self):
        self.nab_cards = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.mast = iter(["пик", "треф", "бубен", "червей"])
        self.curmast = next(self.mast)
        self.cards = iter(self.nab_cards)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curmast:
            raise StopIteration
        if not self.cards:
            self.curmast = next(self.mast)
            self.cards = iter(self.nab_cards)
        return f'{next(self.cards)} {self.curmast}'


cards = list(CardDeck())

print(cards)
