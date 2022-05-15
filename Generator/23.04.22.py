
# generate only the strings with odd length in the given list

names = ["bob", "steve", "alex", "maya", "john"]
# def odd_length():
#     for i in names:
#         if len(i)%2!=0:
#             yield (i)
#
# x = odd_length()
# print(list(x))

#..............................................generator explression

# odd_ = (item for item in names if len(item)%2!=0)
# print(list(odd_))


# generate a tuple of only numeric values in the given list

items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]
#
# def numeric(items_):
#     for i in items_:
#         if isinstance(i, (int, complex, float)):
#             yield i
#
# x = numeric(items)
# print(list(x))


#generator explression

# res = (item for item in items if isinstance(item, (int, float, complex)))
# print(list(res))
#
# res = (item for item in items if isinstance(item, (int, float, complex)))
# print(tuple(res))


# Generating List of PI values with increasing decimal point numbers up to user defined number.. (not understood)
# import math
# PI = math.pi
# print(PI)
#
# def pi_gen(num_of_decimals):
#     for i in range(num_of_decimals):
#         yield round(PI, i)
#
# print(list(pi_gen(4)))

#.........................................................................next

# def sample(a, b):
#     yield a + b
#     yield a
#
#
# res = sample(1, 2)      # generator object
# print(res)
# print(list(res))
# print(next(res))
# print(next(res))
# print(next(res))


# #........................... generate square numbers of given list
# l = [1, 2, 3, 4]
# def squares(list_):
#     for item in list_:
#         yield item ** 2
#
# res = squares(l)
# print(list(res))
#
# res = squares(l)
# print(tuple(res))
#
# res = squares(l)
# print(set(res))
#
# res = (i**2 for i in l)
# print(list(res))
#
# res = (i**2 for i in l)
# print(tuple(res))
#
# res = (i**2 for i in l)
# print(set(res))


# l = [3, 4, 5 ,7]
# def add(a):
#     for i in a:
#         yield i**2
# print(list(add(l)))
#output - [9, 16, 25, 49]

# x=add(l)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

#output -
# 9
# 16
# 25
# 49


