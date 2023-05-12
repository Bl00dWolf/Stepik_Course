names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

# films = {name: boxof - buget for name, buget, boxof in zip(names, budgets, box_offices)}
# [print(f'{name}: {profit}$') for name, profit in sorted(films.items())]
#
# еще вариант
# for name, budgets, box_offices in sorted(zip(names, budgets, box_offices)):
#     print(f'{name}: {box_offices - budgets}$')