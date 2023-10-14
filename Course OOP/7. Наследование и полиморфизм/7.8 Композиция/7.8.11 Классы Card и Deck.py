import random


class Card:
    suits_weights = {'♣': 0, '♢': 1, '♡': 2, '♠': 3}
    ranks_weights = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11,
                     'A': 12}

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    def __init__(self):
        self._deck_ = [Card(suit, rank) for suit in Card.suits_weights for rank in Card.ranks_weights]

    def __repr__(self):
        return f'Карт в колоде: {len(self._deck_)}'

    def shuffle(self) -> None:
        if len(self._deck_) == 52:
            random.shuffle(self._deck_)
        else:
            raise ValueError('Перемешивать можно только полную колоду')

    def deal(self) -> Card:
        if self._deck_:
            return self._deck_.pop()
        raise ValueError('Все карты разыграны')
