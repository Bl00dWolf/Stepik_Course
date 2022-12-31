import sys

en = 'AaBCcEeHKMOoPpTXxy'
ru = 'АаВСсЕеНКМОоРрТХху'

data = [d.strip() for d in sys.stdin.readlines()]
rus = list(filter(lambda x: x in ru, data))
eng = list(filter(lambda x: x in en, data))

if len(rus) and len(eng):
    print('mix')
elif len(rus):
    print('ru')
elif len(eng):
    print('en')