fword = input()
# мап, каждую букву слова превращаем в 0 если согласная, 1 если гласная
fword_indx = list(map(lambda x: 1 if x.lower() in 'ауоыиэяюёе' else 0, fword))
fword_indx_last_glasn = [index for (index, bukva) in enumerate(fword_indx) if bukva == 1]

n = int(input())
words = [input() for _ in range(n)]
# аналогично превращаем в 0, 1 у введенных слов, но до последней гласной в fword_indx
words_indx = [list(map(lambda x: 1 if x.lower() in 'ауоыиэяюёе' else 0, w))[:fword_indx_last_glasn[-1] + 1] for w in
              words]

for i in range(len(words_indx)):
    # если слово из words_indx совпадает с искомым в fword_indx, то печаем это слово - words[i]
    if words_indx[i] == fword_indx[:fword_indx_last_glasn[-1] + 1]:
        print(words[i])

# Изящное решение
# vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# pattern = [i for i, c in enumerate(input()) if c in vowels]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(word) if c in vowels] == pattern:
#         print(word)
