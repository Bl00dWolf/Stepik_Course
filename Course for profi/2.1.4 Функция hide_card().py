def hide_card(card_number):
    return '*' * 12 + card_number.replace(' ', '')[12:]