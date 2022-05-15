
"""
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
"""


# x = lambda a : a + 10
# print(x(5))
#output - 15

# s = [2,3,4,5]
# res = lambda l: l**2
# print(list(map(res, s)))
#output - [4, 9, 16, 25]

# s = [2,3,4,5]
# res = lambda l: l**2
# print(list(filter(res, s)))
#output - [2, 3, 4, 5]


l1 = [4, 2, 13, 21, 5]
# list of square of numbers
# lambda function is used to iterate
# over list l1
l2 = list(map(lambda v: v ** 2, l1))
# print list
print(l2)