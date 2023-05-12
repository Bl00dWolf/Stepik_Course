from collections import defaultdict


def wins(pairs):
    ddict = defaultdict(set)
    for winner, loser in pairs:
        ddict[winner].add(loser)
    return ddict


# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))
