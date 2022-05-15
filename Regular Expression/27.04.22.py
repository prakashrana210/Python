

#................. https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/

import re
# l = ['$23.5', "456.#5", '456gh67%^']
# res = []
# for i in l:
#     l = re.findall(r'\d', i)
#     res.append("".join(l))
# print(res)

# l = ['$23.5', "456.#5", '456gh67%^']
# res = []
# for i in l:
#     a = re.findall(r'\d+', i)
#     print(a)
#     res.append(a)
# print(res)

# l = ['$23.5', "456.#5", '456gh67%^']
# l = ['$23.5', "$456.5", '$45.8']
# l = ["$23.5", "45gh6.5", "456gh6.7%"]
# res = []
# for i in l:
#     a = re.findall(r'\d+.\d+', i)
#     res += a
# print(res)


# s = "dfgdg345656$%^"
# res = re.findall(r"\d", s)     # \d = only digit
# print(res)
#
#
# s = "dfgdg345656$%^"
# res = re.findall(r"\D", s)     # \D = except digit
# print(res)
#
#
# s = "dfgdg345656$%^"
# res = re.findall(r"\w", s)     # \d = only digit
# print(res)


# word = "sony12India pvt34 ltd567 bangalore"
#
# x = re.findall(r"\d+", word)
# print(x)
#
# add = 0
# for i in x:
#     add += int(i)
# print(add)



# res = re.findall(r'hello', 'hello world')
# print(res)
# #............. ['hello']
#
# res = re.findall(r'[hello]', 'hello world')
# print(res)
# #............. ['h', 'e', 'l', 'l', 'o', 'o', 'l']


# res = re.findall(r'\d', 'hello22 world23')
# print(res)
# #............... ['2', '2', '2', '3']
#
# res = re.findall(r'[\d]', 'hello22 world23')
# print(res)
# #............... ['2', '2', '2', '3']


# l = re.findall(r'h.', 'hello how are you')
# print(l)
#..... ['he', 'ho']


# l = re.findall(r'h.*', 'hello how are you')
# print(l)
#......... ['hello how are you']


# l = re.findall(r'colou?r', 'color colour')
# print(l)


# l = re.findall(r'[^https?://]', 'https://www.google.com')
# p = "".join(l)
# print(p)
#.... www.google.com


# l = re.findall(r'\..*\.', 'https://www.google.com')
# print(l)
#.... ['.google.']


# l = re.findall(r'\d{3}', "hello 567 you 76")
# print(str(l))
#.............. ['567']

# l = re.findall(r'\d+', "hello 567 you 76")
# print(str(l))
# #............... ['567', '76']


# l = ['$2^3.5', "456.#5", '456gh67%^']
# l = ['$2^3.5', "$45#6.5", '$45.8']
# res = []
# for i in l:
#     a = re.findall(r'\d+\.\d+', i)
#     res += a
# print(res)


# a = re.findall(r'\d+', 'dfdgh$2^34.5')
# add = 0
# for i in a:
#     add += int(i)
# print(add)
#.... 2+34+5 = 41


# k = re.findall(r'\w+y\b', 'hello, why are you here')
# print(k)
#....... ['why']


# k = re.findall(r'\bw.*y\b', 'hello why are you here')
# print(k)
#.......... ['why']


# s = "hello how are you feeling here"
# l = re.findall(r'\b\w+\b', s)
# print(l)
# #........... ['hello', 'how', 'are', 'you', 'feeling', 'here']
#
#
# s = "hello how are you feeling here"
# l = re.findall(r'\b\w{3}\b', s)
# print(l)
# #............ ['how', 'are', 'you']


