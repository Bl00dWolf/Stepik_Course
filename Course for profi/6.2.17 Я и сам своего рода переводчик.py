alf = 'abcdefghijklmnopqrstuvwxyz'
alf_symm, stroka = input(), input()

for c in stroka:
    if c.lower() in alf:
        print(alf_symm[alf.find(c.lower())], sep='', end='')
    else:
        print(c, sep='', end='')
