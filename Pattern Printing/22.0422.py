



# def func(a, b):
#     if a==b:
#         return -1
#     else:
#         return a, b
#
#
# print(func(1,2))
# print(func(2,2))

#l = [2, 3, 5, 4, 6, 7]
l = [2, 3, 5, 4, 6]
# res = []
# for i in range(len(l)):
#     if len(l)%2!=0:
#         if i==len(l)//2:
#             pass
#         else:
#             res.append(l[i])
#     if len(l)%2==0:
#         if i==len(l)//2 or i==(len(l)//2)+1:
#             pass
#         else:
#             res.append(l[i])
# print(res)


# for i in range(2, 4):
#     for j in range(1, i):
#         print(j, end=", ")
# #print(j)

#row = 4
# for row in range(1,5):
#     for i in range(1, row+1):
#         print(i, end=", ")
#     print()

# for i in range(1, 4):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# x = " ))"
# # for row in range(1, 4):
# #     x = str(row) + x
# #     if len(x)>1:
# #         print(" ".join(list(x)


# s = "string"
# l = s.split()
# print(l)


# for i in range(ord("a"), ord("e")):
#     for j in range(ord("a"), i+1):
#         print(chr(j), end=" ")
#     print()


# for row in range(4, 0, -1):
#     print("*" * row)

# for row in range(1, 5):
#     print("*" * row)

# for row in range(1,5):
#     print("* " * row)

# for row in range(1, 5):
#     print(" *" * row)

# for row in range(3, 0, -1):
#     print(f'{"x " * row:^6}')

# for row in range(1, 5):
#     print(f'{"* " * row:^8}')


# for i in range(5, 0, -1):
#     print(f'{"i " * i:^10}')


# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# for i in range(6, 0, -1):
#     for j in range(1, i-1):
#         print(j, end=" ")
#     print()

# for i in range(7, 0, -1):
#     for j in range(1,i-1):
#         print("5", end=" ")
#     print()


# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# for i in range(5, 0, -1):
#     print(f'{"* " * i:^10}')
#
#
# for i in range(2,6):
#     print(f'{"* " * i:^10}')

# def func():
#     for i in range(5, 0, -1):
#         print(f'{"* " * i:^10}')
#     for i in range(2, 6):
#         print(f'{"* " * i:^10}')
#
#
# func()


# for i in range(ord("A"), ord("E")):
#     for j in range(ord("A"), i+1):
#         print(chr(j), end=" ")
#     print()

#
# row = 6
# for i in range(1,row):
#     for j in range(row-1, 0, -1):
#         print(j, end=" ")
#     print()



# for i in range(1, 6):
#     print(f'{" * " * i: >10}')



# for i in range(1, 6):
#     print(f'{" * " * i: ^10}')


# res = " "
# for i in range(1, 6):
#     res = str(i) + res
#     print(f'{res:<10}')

#...................................................................
#output -
1
21
321
4321
54321
#...................................................................

#
# pat = ''
# for i in range(1, 6):
#     pat = str(i) + " "
#     print(f'{pat:>10}')


# res = " "
# for i in range(1, 6):
#     res = str(i) + res
#     print(f"{res:<10}")
# 1
# 21
# 321
# 4321
# 54321


# res = " "
# for i in range(1, 6):
#     res = res + str(i)
#     print(f"{res:<10}")
#  1
#  12
#  123
#  1234
#  12345


# res = " "
# for i in range(1,5):
#     res = res + str(i)
    # print(f"{res:>8}")
    #    1
    #   12
    #  123
    # 1234

# res = " "
# for i in range(1,5):
#     res = str(i) + res
#     print(f"{res:>8}")
   #
   #    1
   #   21
   #  321
   # 4321

# res = " "
# for i in range(1, 5):
#     res = str(i) + res
#     print(f"{res:^8}")

# for i in range(1, 6):
#     print(f"{'* ' * i:^10}")

#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# for i in range(1, 6):
#     print(f"{'* ' * i:<10}")


# for i in range(1, 6):
#     print(f"{'* ' * i:>10}")


# res = " "
# for i in range(1, 6):
#     res = res + str(i)
#     print(f"{res:<10}")

# res = " "
# for i in range(5, 0, -1):
#     res = res + str(i)
#     print(f"{res:<10}")

 # 5
 # 54
 # 543
 # 5432
 # 54321

# res = " "
# for i in range(5, 0, -1):
#     res = str(i) + res
#     print(f"{res:<10}")
# 5
# 45
# 345
# 2345
# 12345


# res = " "
# for i in range(1, 6):
#     res = res + str(i)
#     print(f"{res:>10}")

     #     1
     #    12
     #   123
     #  1234
     # 12345


# res = " "
# for i in range(1, 6):
#     res = str(i) + res
#     print(f"{res:<10}")
# 1
# 21
# 321
# 4321
# 54321


# res = " "
# for i in range(1, 6):
#     res = res + str(i)
#     print(f"{res:<10}")

 # 1
 # 12
 # 123
 # 1234
 # 12345


# res = " "
# for i in range(ord("a"), ord("e")):
#     res = res + chr(i)
#     print(f"{res:<8}")


# res = " "
# for i in range(ord("a"), ord("e")):
#     res = res + chr(i)
#     print(f"{res:<8}")




# class Point:
#     # class data
#     x = 10
#     y = 20
#
#     # to store data(two integers) inside the point class - constructor/initializer.
#     # helps to save the data in the dictionary(instance dictionary).
#     def __init__(self, a, b):
#         # instance data
#         self.a = a
#         self.b = b
#
#     # creating instance methods to manipulate the saved data of the calling instance
#     def reset(self):
#         self.a = 0
#         self.b = 0
#
#     def move(self, dx, dy):
#         self.a = self.a + dx       # self.a += dx
#         self.b = self.b + dy       # self.b += dy
#
#     def sort(self):
#         if self.a > self.b:
#             self.a, self.b = self.b, self.a
#             return self.a, self.b
#         return self.a, self.b
#
#     def total(self):
#         return self.a + self.b

# ************* creating instance of point class *********************
# passing positional arguments
# p1 = Point(1, 2)    # Point.__init__(p1, 3, 4)
# p2 = Point(3, 4)    # Point.__init__(p2, 3, 4)
#
# # passing keyword arguments
# p3 = Point(a=5, b=6)    # Point.__init__(p3, 5, 6)

"""
* calls __init__() internally --> instances will be pointing to a built in dictionary
* data will be stored in the data structure dictionary - all the methods will take this dictionary
as first argument by default(i.e self)
"""

# ************************** Accessing the values of the class *********************
# syntax - (object.variable)
# print(p1.a)     # 1
# print(p1.b)     # 2

# *************************** Accessing functions of the class *************************
# p1.reset()  # resets the data present in only p1
#             # Point.reset(p1) - python internally does this
# p2.reset()  # Point.reset(p2)
# p1.move(0.1, 0.3)       # Point.move(p1, 0.1, 0.3)
#
# print(dir(p1))  # gives the list of operations that can be performed on p1

# *************************** accessing instance dictionary ********************************
""" __dict__ -> returns the instance dictionary """
# modification of the instance dictionary directly is possible but should not be done.

# print(p1.__dict__)      # {"a": 1, "b": 2}
# print(p2.__dict__)      # {"a":3, "b": 4}


# res = " "
# for i in range(1, 11):
#     res = res + str(i) + " "
#     print(f"{res:<4}")


# num = 0
# for i in range(1, 5):
#     for y in range(1, i+1):
#         num += 1
#         print(str(num) + " ", end=" ")
#     print()

# res = ""
# for i in range(1, 5):
#     res += str(i)
#     print(f"{res:<8}")

# res = "* "
# for i in range(4, 1, -1):
#     print(f"{res * i:^8}")
#
#
# for i in range(1, 5):
#     print(f"{'* ' * i:^8}")



#........................................................................................................................



# res = " "
# for i in range(1, 6):
#     res += str(i)
#     print(f"{res:<10}")


# for i in range(1, 6):
#     print("* " * i)


# for i in range(1, 6):
#     print(f'{"* " * i:^10}')


# res = " "
# for i in range(1, 6):
#     res = res + "* "
#     print(f"{res:^10}")


# for i in range(1, 6):
#     print(f"{'* ' * i:>10}")

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# res = ""
# for i in range(1, 6):
#     res += str(i)
#     print(f"{res:<10}")

# 1
# 12
# 123
# 1234
# 12345

# res = ""
# for i in range(1, 6):
#     res += str(i)
#     print(f"{res:<10}")

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     print("* " * i)

# *
# * *
# * * *
# * * * *
# * * * * *


# for i in range(6, 0, -1):
#     print('* ' * i)


# res = " "
# for i in range(5, 0, -1):
#     res = res + str(i)
#     print(f"{res:^10}")


# res = " "
# for i in range(5, 0, -1):
#     print(f"{'* ' * i:^10}")


"""................................................................................................"""


# for row in range(5):
#     for col in range(row+1):
#         print('*', end=" ")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *


# for row in range(1,6):
#     for col in range(row):
#         print('*', end=" ")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *


# for row in range(1,6):
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5





