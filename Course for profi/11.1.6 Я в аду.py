ph_nums = []

# фигня, а не решение =\

for chunk in input().split():
    ch = chunk.split('-')
    ch[0] = ch[0].replace('+', '')
    ch[-1] = ch[-1].replace(',', '').replace('.', '')
    if len(ch) == 5 and ch[0] == '7' and all(map(str.isdigit, ch)) and len(ch[1]) == 3 and len(ch[2]) == 3 and \
            len(ch[3]) == 2 and len(ch[4]) == 2:
        ph_nums.append('-'.join(ch))
    elif len(ch) == 4 and ch[0] == '8' and all(map(str.isdigit, ch)) and len(ch[1]) == 3 and len(ch[2]) == 4 and \
            len(ch[3]) == 4:
        ph_nums.append('-'.join(ch))

for number in ph_nums:
    print(number)
