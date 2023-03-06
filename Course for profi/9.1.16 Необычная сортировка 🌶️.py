print(''.join(
    sorted(sorted(input()), key=lambda x: (x.islower(), x.isupper(), x.isdigit() and int(x) % 2 > 0), reverse=True)))
