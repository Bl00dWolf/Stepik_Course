class CardDeck:
    def __init__(self):
        self.nab_cards = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.nab_mast = ("пик", "треф", "бубен", "червей")
        self.it_card = iter(self.nab_cards)
        self.it_mast = iter(self.nab_mast)
        self.cur_mast = next(self.it_mast)


    def __iter__(self):
        return self

    def __next__(self):
        cur_card = next(self.it_card, -21)
        if cur_card == -21:
            self.cur_mast, self.it_card = next(self.it_mast), iter(self.nab_cards)
            return f'{next(self.it_card)} {self.cur_mast}'
        return f'{cur_card} {self.cur_mast}'


# cards = list(CardDeck())
#
# print(cards)
