

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

# import re
#
# greeting = "hello world, hello worlds, hello worldz"
# x = re.findall(r'hello', greeting)
# print(x)
#
# greeting = "hello world, helLo worlds, hello worldz"
# x = re.findall(r'hello', greeting, re.IGNORECASE)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'e.', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'\.', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'l.d', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'^world', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'o.*d', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'o.*r', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, hello worldz"
# x = re.findall(r'o.+r', 'or')
# print(x)
#
# greeting = "hello world, he.llo worlds, rs.150 hello worldz"
# #x = re.findall(r'[0-9]', greeting)
# #or x = re.findall(r'\d', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, rs.150 hello worldz"
# #x = re.findall(r'[^0-9]', greeting)
# #or x = re.findall(r'\D', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, rs.150 hello worldz"
# x = re.findall(r'[aeiou]', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, rs.150 hello worldz"
# x = re.findall(r'[^aeiou]', greeting)
# print(x)
#
# greeting = "hello world, he.llo worlds, rs.150 hello worldz"
# x = re.findall(r'\b\d{3}\b', greeting)
# print(x)
#
# x = re.findall(r'\w{3}', 'helloworld')
# print(x)
#
# x = re.findall(r'\w{3,5}', 'helloworld')
# print(x)
#
# greeting = "hello world, he.llo worlds, rs.150 hello worldz"
# y = re.findall(r'[^0-4]', greeting)
# print(y)


# l = ["def", "gh", "abc"]
# print(sorted(l))

d = {"def":1, "gh":3, "abc":2}
print(sorted(d))
print(sorted(d.keys()))
print(dict(sorted(d.items())))
print(sorted(d.values()))

# d = {"a": 20, "b": 5, "c": 20}
# d1={}
# for i,v in d.items():
#     if v not in d1.values():
#         d1[i] = v
# res = sorted(d1.items(), key = lambda i: i[-1])
# print(dict[((res[-2][0]), (res[-2][-1]))])



# d = {"a": 20, "b": 5, "c": 15}
#
# x = sorted(d.items(), key=lambda i: i[-1])
# print(x[-2][-1])
#
# d = {"a": 20, "b": 5, "c": 20}
# x = sorted(d.items(), key=lambda i: i[-1])
# emp = []
# for i in x:
#     if i[-1] not in emp:
#         emp.append(i)
# print(emp)
# x = dict([(emp[0]), (emp[1])])
# print(x)

# d = {"a": 20, "b": 5, "c": 20}
# d1 = {}
# for key, value in d.items():
#     if d[key] not in d1.values():
#         d1[key] = value
#
# res = sorted(d1.items(), key=lambda item: item[-1])
# print(res[-2])

# word = '@hello12sed gy%^*hk bhg'
# x = re.findall(r'\w', word)
# print(x)


#
# l = [2,4,5,6,7]
# def even(num):
#     if num%2==0:
#         return num
# evens_ = map(even, l)
# print(list(evens_))
# evens__ = filter(evens_, l)
# print(evens__)

# number = filter(even, l)
# print(number)

# import time
#
# def outer_most(n):
#     def outer(func):
#         def inner(*args, **kwargs):
#             time.sleep(n)
#             print(func(*args, **kwargs))
#         return inner
#     return outer
#
# @outer_most(3)
# def add(*x):
#     return a+b
#
# add(1,2)
#
# @outer_most(5)
# def sub(*y):
#     return a-b
#
# sub(3,2)


# class father:
#     def __init__(self, fname, mname):
#         self.a = fname
#         self.b = mname
#
#     def name(self, lname='rana'):
#         self.lname = lname
#
# class mother(father):
#     pass
#
# class child(father):
#     def name(self):
#         super().name(self, lname='rana')
#
# f = father('gopal', 'singh')
# c = child('shiv', 'prakash')
# c.name()


for i in range()

