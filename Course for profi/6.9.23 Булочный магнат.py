from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().lower().split(','))
max_len_ingr = len(max(order.keys(), key=len))

max_len_str, total = 0, 0
for ingr, count in sorted(order.items()):
    line = f'{ingr.ljust(max_len_ingr)} x {count}'
    total += ingredients[ingr] * count
    if len(line) > max_len_str:
        max_len_str = len(line)
    print(line)

tl_phrase = f'ИТОГ: {total}р'
if len(tl_phrase) > max_len_str:
    max_len_str = len(tl_phrase)

print(f'{"-" * max_len_str}\n{tl_phrase}')