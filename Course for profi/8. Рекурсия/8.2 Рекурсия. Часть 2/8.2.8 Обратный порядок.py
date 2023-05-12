def print_reverse(listek: list) -> None:
    def pr_cur(num):
        if num >= 0:
            print(listek[num])
            pr_cur(num - 1)

    pr_cur(len(listek) - 1)


listochek = []
curs = ''
while curs != '0':
    curs = input()
    listochek.append(curs)

print_reverse(listochek)


# еще вариант хороший
# def recursion():
#     digit = int(input())
#     if digit != 0:
#         recursion()
#     print(digit)
#
# recursion()