def card_deck(suit: str):
    card_values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
    card_mast = ["пик", "треф", "бубен", "червей"]
    if suit and suit in card_mast:
        card_mast.remove(suit)

    while True:
        for mast in card_mast:
            for card in card_values:
                yield f'{card} {mast}'


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)
