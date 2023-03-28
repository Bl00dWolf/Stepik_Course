def cubes_of_odds(iterable):
    return (number ** 3 for number in iterable if number % 2)