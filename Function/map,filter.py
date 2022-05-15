
"""https://github.com/vidyagowda159/Alpha-4/blob/master/Functions/anonymous_functions/filter.py"""

# MAP - CONDITION AND EXPRESSION BOTH
# Filter - only condition , does not perform on expression

# a  = [2,3,4,5,6,7]
# def func(l):
#     if l%2==0:
#         return l**2

# res = map(func, a)
# print(list(res))
"""output - [4, None, 16, None, 36, None]"""

# res = filter(func, a)
# print(list(res))
"""output - [2, 4, 6]"""

# res = filter(func, a)
# emp = map(func, res)
# print(list(emp))
"""output - [4, 16, 36]"""

# res  = map(func, a)
# emp = filter(func, res)
# print(list(emp))
"""output - TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'"""


#.......................................................


# a = [10, 20, 30, 40, 0]
# def func(n):
#     return n+2

# res = map(func, a)
# print(list(res))
"""output - [12, 22, 32, 42, 2]"""

# res = filter(func, a)
# print(list(res))
"""output - [10, 20, 30, 40, 0]"""

# res = map(func, a)
# emp = filter(func, res)
# print(list(emp))
"""output - [12, 22, 32, 42, 2]"""

# res = filter(func, a)
# emp = map(func, res)
# print(list(emp))
"""output - [12, 22, 32, 42, 2]"""



