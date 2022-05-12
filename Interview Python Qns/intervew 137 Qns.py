

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
# path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txt"
#
#
# # with open(path) as file:
# #     print(list(islice(file, 1, 2)))

""" 12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line) """

# with open(path) as file:
#     print(list(islice(file, 4, 7)))

""" 13 Program to print last "N" lines of a file. """

# path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txt"

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

# a = [1, 2, 3, 4, 5]

# def func(l):
#     b = l[::-1]
#     print(b)
#
# func(a)


""" 35 Write a function to print the below output. """ #....................................Not Done
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX


#sys.float_info.epsilon

# def func(s, p):
#     b = s[p:]
#     print(b)
#
# func("TRACXN", 0)
# func("TRACXN", 1)



""" 36 Sum all the numbers in the below string. """
# s = "Sony12India567Pvt2ltd"
# add = 0
# for i in s:
#     if i.isdigit():
#         add += int(i)
# print(add)

# s = "Sony12India567Pvt2ltd"
#
# class solution:
#     def st(self, p):
#         self.p = p
#         self.add = 0
#         for i in p:
#             if i.isdigit():
#                 self.add += int(i)
#         print(self.add)
#
# x = solution()
# x.st(s)


""" 38 Print all the numbers in the below list """
# a = ['abc', '123', 'hello', '23']
# res = []
# for i in a:
#     if i.isdigit():
#         res.append(i)
# print(res)


""" 39 Program to print the number of occurrences of characters in a String without using inbuilt functions. """

# s = 'helloworld'
# from collections import defaultdict
# dd = defaultdict(int)
# for i in s:
#     dd[i] += 1
# print(dd)



""" 40 Program to print only the repeated characters and count of the same. """
# s = 'helloworld'
# for i in s:
#     print(i, s.count(i), sep="-")



""" 41 Write a program to get alternate characters of a string in list format. """
# s = 'hello world welcome to python'
# for i in range(len(s)):
#     if i%2 == 0:
#         print(s[i], end="")


""" 42 Write a program to get square of list of number's using lambda function . """ #.................not done

# l = [2,3,4,5]
# x = lambda i: i**2
# print(filter(x, l))

# def func():
#     for i in a:
#         res = i**2
#     print(res)
#
# func(l)



""" 43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other. """

# def func(a, b):
#     if sorted(a) == sorted(b):
#         return a, "and", b, "are anagram"
#     return a, b, "and", "are not anagram"
#
# print(func("eat", "tea"))
# print(func("bag", "gag"))



""" 44 Write a program to iterate through list and build a new list, only if the items of the list has even number of 
characters."""

# res = []
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# for i in names:
#     if len(i)%2 == 0:
#         res.append(i)
#
# print(res)


""" 45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even 
number of characters. """

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {}
# for i in names:
#     if len(i)%2==0:
#         d[i] = len(i)
# print(d)


""" 46 Write a program which squares the numbers in a list using map object """ #...........................not done

# l = [3,4,5,6]
# def func(a):
#     res = []
#     for i in a:
#         res.append(i**2)
#     print(res)
#
# func(map(l))



""" 47 Count number of lines in a file without loading the file to the memory """ #............................not done

file = '''hello python hello world
gold world python laugh happen laugh out loud
tea bag hai
parent family member youngest'''

# count = 0
# # print(file.split("\n"))
# for line in file.split("\n"):
#     count += 1
#
# print(count)


""" 49 Write a Program to print the sum of entire list and sum of only internal list """
# l = [[1,2,3],[4,5,6],[7,8,9]]
#
# entire_sum = 0
# for i in l:
#     inner_sum = 0
#     for j in i:
#         inner_sum += j
#     print(inner_sum)
#     entire_sum += inner_sum
# print(entire_sum)


""" 50 Write a program to reverse the list as below """

# words = ["hi", "hello", "python"]
#
# res = []
# for i in words[::-1]:
#     res.append(i[::-1])
# print(res)


""" 51 Write a program to update the tuple """


""" 52 Write a program to replace value present in nested dictionary. """



""" 53 Write a program to count the number of white spaces in a file. """

# for i in file:
#     a = file.count(" ")
# print(a)

# count = 0
# for i in file:
#     if i == " ":
#         count += 1
# print(count)


""" 54 Grouping anagrams. """ #............................................................................not done
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# line = words.copy()
# from collections import defaultdict
# dd = defaultdict(list)
# for i in words:
#     for j in line:
#         if sorted(i) == sorted(j) and dd.values() not in dd:
#             dd['anagram'] += [i]
#         dd['not anagram'] += [i]
#         words.remove(i)
#         line.remove(j)
# print(dd)



""" 56 Explain property decorator in python. """

# def func(spam):
#     def inner(spam(a)):
#         b = spam(a) + 5
#     return b
#
# @func
# def spam(a):
#     return a
#
# print(spam(10))

# def spam(func):
#     def inner(func(a,b)):
#         c = func(a,b) * 5
#     print(c)
#
#
# def func(a, b):
#     return a+b
#
# func(4,5)


""" 58 Explain get() method in dictionaries. """

# d = {"a":2, "b":3, "c":4, "d":5}
# print(d.values())
# print(d.items())



""" 59 Write a list comprehension to get a list of even numbers from 1-50 """

# l = [i for i in range(1, 51) if i%2==0]
# print(l)


""" 60 Find the longest non-repeated substring in the below string """ #.................................not done

# s = "hello world python here python here world "
# res = sorted(set(s), key = lambda i: len(i))
# # print(res)
# print(res[-1])



""" 61 Write a program to find the duplicate elements in the list without using inbuilt functions """
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# res = []
# for i in names:
#     if names.count(i)>1 and i not in res:
#         res.append(i)
# print(res)


""" 62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions """
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# from collections import defaultdict
# dd = defaultdict(int)
# for i in names:
#     dd[i] += 1
# print(dd)


""" 63 Write a function to check if the number is Prime """

# a = 7
# for i in range(1, a):
#     if a%i==0:
#         print(a, "is prime number")
#         break
#     print(a, "is prime number")


# res = []
# for i in range(1, 51):
#     for j in range(2, i):
#         if i%j == 0:
#             break
#     else:
#         res.append(i)
# print(res)


""" 64 How to create a tuple using range function """ #.....................................................Not Sure
# res = []
# for i in range(1, 11):
#     res.append(i)
# print(tuple(res))


""" 65 Write a program to find the largest number in the list without using any inbuilt functions """

# numbers = [10, 20, 30, 50, 40]
# largest = 0
# for i in numbers:
#     if i > largest:
#         largest = i
# print(largest)



""" 66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) 
should return 2."""

# a = 3572
# def func(l):
#     s = str(l)
#     for i in range(len(s)-1, -2, -1):
#         return s[i]
#
# print(func(a))



""" 67 Write a program to find most common words in a given list. """



""" 68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns 
the last n elements from the given sequence, as a list."""


# a = "consonant"
# res = []
# def func(l, p):
#     for j in range(-1, -4, -1):
#         res.append(l[j])
#     return res
#
# print(func(a, 3))


""" 69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and 
False if it's not. """

#.a
# def func(n):
#     for i in range(n):
#         if i*i==n:
#             return n, "is perfect squire"
#     return n, "is not a perfect squire"
#
# print(func(9))
# print(func(8))

#.b
# def func(n):
#     if int(n**1.5)*int(n**1.5) == n:
#         print(n, "is perfect squire")
#     print(n, "is not perfect squire")
#
# func(8)
# func(9)


""" 70 Write a program to get all the duplicate items and the number of times the item is repeated in the list. """
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d = {}
# for i in names:
#     if names.count(i)>1:
#         d[i] = names.count(i)
# print(d)
#
# from collections import defaultdict
# dd = defaultdict(int)
# for i in names:
#     if names.count(i)>1:
#         dd[i] += 1
#
# print(dd)


""" 71 Write a program to count the number of occurrences of each word in a file. """

# file = '''hello python hello world
# gold world python laugh happen laugh out loud
# tea bag hai
# parent family member youngest'''
# d = {}
# for i in file.split("\n"):
#     for j in i.split():
#         d[j] = i.split().count(j)
# print(d)


""" 72 Write a program to count the number of occurrences of vowels in a file. """
file = '''hello python hello world
gold world python laugh happen laugh out loud
tea bag hai
parent family member youngest'''

#.....................................correct
# from collections import defaultdict
# dd = defaultdict(int)
# for i in file.split("\n"):
#     for j in i.split():
#         for r in j.split():
#             for k in list(r):
#                 if k in "aeiouAEIOU":
#                     dd[k] += 1
# print(dd)


#..................................not correct
# d = {}
# for i in file.split("\n"):
#     for j in i.split():
#         for r in j.split():
#             for k in list(r):
#                 if k in "aeiouAEIOU":
#                     d[k] = list(r).count(k)
# print(d)


# """ 73 Write a program to print all numeric values in a list """
# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# res = []
# for i in items:
#     if isinstance(i, (int, float, complex)):
#         res.append(i)
#
# print(res)


""" 74 Triangle Patterns """

# for i in range(1, 6):
#     print(f"{'* ' *i:^10}")


""" 75 Write a program count the occurrence of a particular word in the file """

# path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Interview Python Qns\sample.log"
# d={}
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             for word in line.split():
#                 d[word] = line.count(word)
# print(d)


""" 76 Write a program to map a product to a company and build a dictionary with company and list of products pair """

# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# from selenium.webdriver import ActionChains
#
# from time import sleep
#
# driver.get("https://www.ajio.com/?gclid=Cj0KCQjwr-SSBhC9ARIsANhzu150QXewGeFPYjitvO7uxQ0H1nnSshVCXQOZLOJmP5ncXPSlSZh1iYEaAsjaEALw_wcB").click()
#
# action = ActionChains(driver)
# # driver.implicitly_wait(4)
# x = action.move_to_element(driver.find_element_by_xpath("//a[@title='MEN']")).perform()
# # action.move_to_element(driver.find_element_by_xpath("//span[text()='CLOTHING']")).click().perform()
# x.click()

""" 77 Write a program to rotate items of the list """
names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

# from itertools import zip_longest
# a = ["aa", 'bb', "cc", "ff"]
# b = ["dd", "ee"]
    # res = [(i,v) for i,v in zip_longest(a, b)]
    # d = {i:v for i,v in zip_longest(a, b)}
    # print(res)
    # print(d)

# d = {}
# for i in a:
#     for j in range(len(b)):
#         d[i] = b[j]
# print(d)

""" 77 Write a program to rotate items of the list """
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# for i in names:



""" 78 Write a program to rotate characters in a string """
# heck = "hello world"
# l = list(heck)
# for i in range(len(l)):
#     l.insert(i, l.pop(-(i+1)))
#     l.insert(-(i+1), l.pop(i-1))
# print(l)


""" 79 Write a program to count the number of white spaces in a given string """

# s = "hello world python here"
# class count:
#     def count_(self):
#         for self.i in s:
#             return s.count(" ")
#
# x = count()
# print(x.count_())


# s = "hello world python here"
# def count():
#     for i in s:
#         return s.count(" ")
# print(count())


# count = 0
# for i in s:
#     if i == " ":
#         count += 1
# print(count)


""" 80 Write a program to print only non-repeated characters in a string """

# s = "hello world python"
# res = " "
# for i in s:
#     if s.count(i) == 1:
#         res += i
#
# print(res)


""" 82 Write a program to print all the consonants in a given string """
# s = 'helloworld'
# res = " "
# for i in s:
#     if i not in "aeiouAEIOU":
#         res += i
#
# print(res)


""" 83 Write a program to count the number of commented lines in a text file """ #...............................




""" 84 Write a program to check if the year is leap year or not """

# year = 2020
# if year%4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# def year_(year):
#     if str(year)[-2:] not in "00" and year % 4 == 0:
#         print(year, "is a leap year")
#     elif str(year)[-2:] in "00" and year%400 == 0:
#         print(year, "is a leap year")
#     else:
#         print(year, "is not a leap year")
# year_(2020)
# year_(2021)
# year_(1900)
# year_(2000)
# year_(2024)


""" 85 Liner Search """


""" 86 Difference between xrange and range """


""" 87 Write a program to count no of capital letters in a string """
# s = "Hello worLd wE aRe HeRE"
# count = 0
# for i in s:
#     if i.isupper():
#         count += 1
#
# print(count)


""" 88 Write a program to get the below output """

# for i in range(1, 5):
#     print('* '*1)
#     j = i + 1
#     print('* '*j)


""" 89 Write a program to get the below output """

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in a:
#     print([a[i], a[i+1]])



""" 90 Write a program to check if the elements in the second list is series of continuation of the items in the 
first list """

# a = [10, 12, 14, 16, 18]
# b = [20, 22, 23, 26, 28]
# c = a+b
# diff = c[1]-c[0]
# def series():
#     for i in range(len(c)-1):
#         if c[i+1]-c[i] != diff:
#             return "series is not continuation"
#     return "series is continuation"
#
# print(series())


# n = 12
# def prime():
#     i = 2
#     while i<n or i>n:
#         if n%i == 0:
#             break
#     if n%i != 0:
#                 return n "is "


""" 91 What is the difference between append() and extend() method in list """

#..append add the element in the list at the last position. extend insert all elements in the list at the last position.


""" 92 Write a program to find the first repeating character in a string """
# s = 'helloworld'
# for i in s:
#     if s.count(i)>1:
#         print(i)
#         break


""" 93 Write a program to find the index of nth occurrence of a sub-string in a string """ #...................wrong

# s = 'helloworld'
# ss = input("alphabet:")
# ind = int(input("occurance:"))
# for i in range(len(s)):
#     if i == ss:
#         print(i, s[i])



""" 97 Write a program to count the number of occurrences of non-special characters in a given string """

# res = []
# for i in range(51):
#     for j in range(2, i):
#         if i%j==0:
#             break
#     else:
#         res.append(i)
# print(res)


""" 95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd 
numbers first and then even numbers in sorted order"""
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# b = [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]
# odd = []
# even = []
# for i in a+b:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# odd_ = sorted(odd)
# even_ = sorted(even)
#
# odd_.extend(even_)
# print(odd_)

""" 96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers 
# should be in ascending order and even numbers should be in descending order"""
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# b = [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]
# odd = []
# even = []
# for i in a+b:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# odd_ = sorted(odd)
# even_ = sorted(even, reverse=True)
# odd_.extend(even_)
# print(odd_)


""" 98 Grouping Flowers and Animals in the below list """ #..............................................wrong
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# from collections import defaultdict
# dd = defaultdict(list)
# for i in items:
#     for _ in i.split('-'):
#         dd[i[-1]] += i[0]
# print(dd)


"""94 Write a program to print prime numbers from 1 to 50"""


#...................................................................not working
# def prime_(n):
#     flag = True
#     for i in range(1,n):
#         if n%i == 0:
#             break
#
#     if flag:
#         return True
#     else:
#         return False
# m = filter(map(prime_, range(1, 51)))
#
# for i in m:
#     print(i)



""" 99 Grouping files with same extensions """
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# from collections import defaultdict
# dd = defaultdict(list)
# for i in files:
#     k = i.split(".")
#     for j in k:
#         dd[k[-1]] += k[0]
# print(dd)


""" 100 Filter only those characters except digits """
# s = '@hello12world34welcome!123'
# import re
# l = re.findall(r"/d", s)
# print(l)


""" 101 Count number of words in a sentence. ignore special characters. """
sentence = "Hi there! How are you:) How are you doing today!"



""" 102 Grouping even and odd numbers """
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}
# from collections import defaultdict
# dd = defaultdict(list)
# for i in numbers:
#     if i%2 != 0:
#         dd[1] += [i]
#     else:
#         dd[0] += [i]
# print(dd)


""" 103 Find all max numbers from the below list """
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# # Output should be [4, 4, 4]
# l = max(numbers)
# for i in numbers:
#     if i == l:
#         print(i, sep=", ", end=" ")
#
# print()


""" 104 Find all max length words from the below sentence """
# sentence = "hello world hi apple you yahoo to you"
# l = sentence.split()
# res = []
# for i in l:
#     res.append(len(i))
# p = max(res)
# for i in res:
#     if i == p:
#         print(i, sep=", ", end=" ")


""" 105 Find the range from the following string """
# sentence = '0-0, 4-8, 20-20, 43-45'
# # Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
#
# l = sentence.split()
# res = []
# for i in l:
#     for j in i.split("-"):
#         res.append(range(int(i.split("-")[0]), int(i.split("-")[-1])+1))
# print(res)










''''''''''''''''''

s = "(([{}))"

''''''''''''''''''



# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# from selenium.webdriver.common.action_chains import ActionChains
#
# from time import sleep
#
# driver.get("https://www.ajio.com")
# action = ActionChains(driver)
# driver.implicitly_wait(30)
# x = action.move_to_element(driver.find_element_by_xpath("//a[@title='MEN']")).perform()
# # action.move_to_element(driver.find_element_by_xpath("//span[text()='CLOTHING']")).click().perform()
# x.click()





























































































""" 55 What is the difference between defaultdict and normal dictionary. """































































































