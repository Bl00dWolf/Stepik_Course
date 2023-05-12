from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]


ddict = defaultdict(int)
for key, value in data:
        ddict[key] += value

[print(f'{key}: ${value}') for key, value in sorted(ddict.items(), key=lambda x: x[0])]