from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
         date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]

quartal = {'Q1': (1, 2, 3), 'Q2': (4, 5, 6), 'Q3': (7, 8, 9), 'Q4': (10, 11, 12)}
quartal_tuple = ('Q1', 'Q2', 'Q3', 'Q4')

for d in dates:
    for q in quartal_tuple:
        if d.month in quartal.get(q):
            print(f'{d.year}-{q}')
