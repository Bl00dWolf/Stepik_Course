import re
import keyword

data = input()

for kword in keyword.kwlist:
    data = re.sub(fr'\b{kword}\b', r'<kw>', data, flags=re.IGNORECASE)
print(data)

# еще вариант
# import re
# import keyword
#
# keys = '|'.join(keyword.kwlist)
#
# print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))