import sys

num, *data = [set(s.strip().replace(' ', '').split(',')) for s in sys.stdin.readlines()]

lang_set = data[0]
for sset in data:
    lang_set.intersection_update(sset)

if lang_set:
    print(*sorted(lang_set), sep=', ')
else:
    print('Сериал снять не удастся')