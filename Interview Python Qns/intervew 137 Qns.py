

# from selenium webdriver import Chrome
# from time import sleep
# #import csv
# #import re
# from selenium.common.exceptions import NoSuchElementExecption
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.excepted_conditions import visisbilty_of_element_located
# from selenium.webdriver.remote.webelement import WebElement



""" 11. Write a program to read a random line in a file. (ex. 50, 65, 78th line) """

# from itertools import islice
#
# import os
#
# path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Programme\File.Handling\Text_log_files\sample.txt"
#
#
# # with open(path) as file:
# #     print(list(islice(file, 1, 2)))

""" 12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line) """

# with open(path) as file:
#     print(list(islice(file, 4, 7)))

""" 13 Program to print last "N" lines of a file. """

# path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Programme\File.Handling\Text_log_files\sample.txt"

# from collections import deque
# with open(path) as file:
#     print(list(deque(file, 3)))

#output - ['programming in python is fun 5\n', 'java is fun 6\n', 'python is easy 7\n']


""" 14. Write a program to check if the given string is Palindrome or not without using reversed method. """

# s = "malayalam"
# if s == s[::-1]:
#     print(s, "is pallindrne")
# else:
#     print(s, "is nt pallindrne")


""" 15 Write a program to search for a character in a given string and return the corresponding index. """

#..a

# l = "string"
# for i in range(len(l)):
#     print(i, l[i], sep="-")

#..b

# l = "string"
# for i,v in enumerate(l):
#     print(i, v, sep="-")

#...................................................................................................................
""" 16 Write a program to get the below output """
# sentence = "hello world welcome to python programming hi there"



""" 17 Write a to replace all the characters with - if the character occurs more than once in a string """

# l = "consonant"
# res  = " "
# for i in l:
#     if i in res:
#         res += "-"
#     else:
#         res += i
# print(res)


""" 18 write a decorator that returns only positive values of subtraction """


# def decor(value):
#     def inner(n):
#         return abs(value(n))
#     return inner
#
# @decor
# def func(n):
#     return n
#
# print(func(-2))

#....................................................................................................................
""" 19 How to get the count of number of instances of a class that is being created. """



""" 20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and 
if the item is integer of float it should reverse it. """

#.a
# l = ["ab", "cd", 23, 34, "ef"]
# def func():
#     app = []
#     for i in l:
#         if isinstance(i, str):
#             app.append(i)
#         else:
#             app.append(int(str(i)[::-1]))
#     print(app)
# func()


#output - ['ab', 'cd', 32, 43, 'ef']

#.b

# l = ["ab", "cd", 23, 34, "ef"]
# def func(p):
#     app = []
#     for i in p:
#         if isinstance(i, str):
#             app.append(i)
#         else:
#             app.append(int(str(i)[::-1]))
#     print(app)
# func(l)

#.c

l = ["ab", "cd", 23, 34, "ef"]

# def func(*p):
#     app = []
#     for i in p:
#         if isinstance(i, str):
#             app.append(i)
#         else:
#             app.append(int(str(i)[::-1]))
#     print(app)
# func(*l)

#output - ['ab', 'cd', 32, 43, 'ef']

#.d......................................................error

         #output - TypeError: func() takes 1 positional argument but 5 were given


l = ["ab", "cd", 23, 34, "ef"]

# def func(p):
#     app = []
#     for i in p:
#         if isinstance(i, str):
#             app.append(i)
#         else:
#             app.append(int(str(i)[::-1]))
#     print(app)
# func(*l)

#output - TypeError: func() takes 1 positional argument but 5 were given

#..................................................................................................................
""" 21 Write a class named Simple and it should have iteration capability. """


#..................................................................................................................
""" 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a """



""" 23 Write a python program to get the below output """



""" 24 Write a python program to get the below output """



""" 25 Write a lambda function to add two numbers (a, b) """

# res = lambda a,b: a+b
# print(res(2,3))

#output - 5

""" 26 What is the output of the following """
a = [1, 2, 3]
b = [4, 5, 6]

# print([a, b])
# #output - [[1, 2, 3], [4, 5, 6]]
#
# print((a, b))
# #output - ([1, 2, 3], [4, 5, 6])


""" 27 How to remove duplicates from the list without using inbuilt functions """
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]

#.a

print(list(set(items)))
#output - [1, 2, 3, 4, 5]

#.b

# app = []
# for i in items:
#     if i not in app:
#         app.append(i)
# print(app)

#output - [1, 2, 3, 4, 5]


""" 28 Find the longest word in the sentence """

# sentence = "Hello world. Welcome to Python"
# l = sentence.split()
# res = sorted(l, key=len)
# print("longest", "-", res[-1])

#output - longest - Welcome


""" 29 write a program to reverse the values in the dictionary if the value is of type String """

d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# res = {i:v[::-1] if isinstance(v, str) else v for i,v in d.items()}
# print(res)

#output - {'a': 'olleh', 'b': 100, 'c': 10.1, 'd': 'dlrow'}


""" 30 write a program to get 1234 """

# t = ('1', '2', '3', '4')
# print(int("".join(list(t))))

#output - 1234


""" 31 How to get the elements that are in list b but not in list a """
a = [1, 2, 3]
b = [1, 2, 3, 4]

# print(set(b).difference(set(a)))


""" 32 A function takes variable number of positional arguments as input. How to check if the arguments that are 
passed are more than 5 """

# def func(*l):
#     if len(l) > 5:
#         print("len is more than 5")
#     else:
#         print("len is <= 5")
# func(1,2,3,4,5,6)

#output - len is more than 5


#........................................................................................................

""" 33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file. """
lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""



""" 34 Write a function to reverse any iterable without using reverse function. """

a = [1, 2, 3, 4, 5]

# def func(l):
#     b = l[::-1]
#     print(b)
#
# func(a)


""" 35 Write a function to print the below output. """
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX


#sys.float_info.epsilon

# def func(s, p):
#     b = s[p:]
#     print(b)
#
# func("TRACXN", 0)
# func("TRACXN", 1)


















































