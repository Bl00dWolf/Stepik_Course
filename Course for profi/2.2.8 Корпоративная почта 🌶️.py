domain = '@beegeek.bzz'

mails = [input() for _ in range(int(input()))]

print(mails)

for _ in range(int(input())):
    nmail = input()
    if nmail + domain not in mails:
        mails.append(nmail + domain)
    # else:
    #     mails.append(nmail + )