

# a = 2
# b = 0
# try:
#     d = a/b
#     print(d)
# except ZeroDivisionError:
#     print("zero is not allowed")
# else:
#     print("else")
# finally:
#     print("finally")
#
# print()

# a = 2
# b = 1
# try:
#     d = a/b
#     print(d)
# except ZeroDivisionError:
#     print("zero is not allowed")
# else:
#     print("else")
# finally:
#     print("finally")


# def disp(a, b):
#     yield a
#     yield b

# x, y = disp(10, 20)
# print(x)
# print(y)

# x = disp(10, 20)
# print(list(x))

# result = disp(10, 20)
# print(result)
# print(type(result))

#.........................................generator

# l = [2,3,4,5,6]
#
# def disp(*a):
#     for i in a:
#         yield i
#
# result = disp(*l)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

#.......................................

import re

greeting = "hello world, hello worlds, hello worldz"
x = re.findall(r'hello', greeting)
print(x)

greeting = "hello world, helLo worlds, hello worldz"
x = re.findall(r'hello', greeting, re.IGNORECASE)
print(x)

greeting = "hello world, he.llo worlds, hello worldz"
x = re.findall(r'e.', greeting)
print(x)

greeting = "hello world, he.llo worlds, hello worldz"
x = re.findall(r'\.', greeting)
print(x)











