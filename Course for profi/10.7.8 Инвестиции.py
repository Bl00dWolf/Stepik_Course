import csv

with open('data.csv', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    ft_rnd_a = (i for i in reader if i['round'] == 'a')
    ft_invested = (int(inv['raisedAmt']) for inv in ft_rnd_a)
    print(sum(ft_invested))