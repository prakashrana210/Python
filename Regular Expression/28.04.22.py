

# word = "sony12INdia A pvt34 ltd567 bangalore"
# l = word.split()
# res = " "
# for i in l:
#     if i.islower():
#         res += i.upper()
#     elif i.isupper():
#         res += i.lower()
#     else:
#         res += i
# print(res)


# import re
# a = "9000.00"
# x = re.findall(r'\d{4,5}', a)
# for i in x:
#     print(int(i))


# b = "hello"
# res = re.findall(r'l+', b)
# print(res)


# import re
# c = re.findall(r'[0-9]+', "how 34 45")
# print(c)

import re

phone_numbers = ['123-234-5678', '1234-456-5678', '455-4564-567']
def func():
    d = []
    for i in phone_numbers:
        x = re.findall(r'\d+', i)
        d += x
    print(d)
func()
