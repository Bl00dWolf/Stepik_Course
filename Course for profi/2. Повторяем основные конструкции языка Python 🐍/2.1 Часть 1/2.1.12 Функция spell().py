def spell(*args):
    spells = dict()
    for word in args:
        spells[word[0].lower()] = len(sorted(args, key=lambda x: len(x) if x[0].lower() == word[0].lower() else 1, reverse=True)[0])
    return spells