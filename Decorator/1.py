
#time decorator


#..

import time

def decor(func):
    def inner():
        start = time()
        result = func()
        end = time()
        print(f"execution time of function {func.__name__} is {end-start} seconds")
        return result
    return inner
@decor
def greet():
    return "hello world"

#print(greet())

# output - this programme will not work because we are importing time module, we will get the below output with error

# File "C:/Users/Admin/PycharmProjects/shiv_prakash/Decorator/1.py", line 18, in <module>
#     print(greet())
#   File "C:/Users/Admin/PycharmProjects/shiv_prakash/Decorator/1.py", line 8, in inner
#     start = time()
# TypeError: 'module' object is not callable

#..........................................................................................

from time import time

def decor(func):
    def inner():
        start = time()
        result = func()
        end = time()
        print(f"execution time of function {func.__name__} is {end-start} seconds")
        return result
    return inner
@decor
def greet():
    return "hello world"

#print(greet())

#output -
# execution time of function greet is 0.0 seconds
# hello world

#..........................................................

# print(time())
# 1645254664.6182168

#..........................................................


from time import sleep


# def delay(func):
#     def wrapper(*args, **kwargs):
#         sleep(5)
#         return func(*args, **kwargs)
#
#     return wrapper

#.Note: with above these 5 lines the code is not getting executed delay

# def log(func):
#     def wrapper(*args, **kwargs):
#         sleep(5)
#         print(f"you are calling {func.__name__}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def greet():
#     return "hello world"
#
#
# greet()

#
# @log
# def greeting(name):
#     return f'hello {name}'
#
#
# greeting('rohit')
#
#
# @log
# def add(a, b):
#     return a + b
#
#
# add(2, 3)

# ..................................................

#................................................................Func count decorator

# from collections import defaultdict
#
# dd = defaultdict(int)
#
# def func_count(func):
#     def wrapper(*args, **kwargs):
#         dd[func.__name__] += 1
#         print (func(*args, **kwargs))
#     return wrapper
# @func_count
# def greet():
#     print ("hello world")
#
# greet()

#..........................................

# def func_count():
#     return

# s = "AABBCCCDAACD"
#
# for i in range(len(s)):
#     print(s.count(i))
#
# # for i in range(len(s)):
# #     if s[i] == s[i+1]:
# #         s.replace(s[i], s.count(i)+s[i])
# #     else:
# #         s.replace(s[i], '1'+s[i])
# # print(s)


#...........................................................


args = ([1234567890, 9087654738, 911234567890, 231234567890])

def add_prefix(func):
    str_number = str(func)
    if len(str_number) == 10:
        str_number = "+91-" + str_number
        return str_number
    elif len(str_number) == 12 and str_number.startswith("91"):
        str_number = "+" + str_number[:2] + "-" + str_number[2:]
        return str_number
    else:
        return str_number

def country_code(func):
    def wrapper(*args, **kwargs):
        temp = args[0]
        processed_numbers = [add_prefix(func) for func in temp]
        return func(processed_numbers)
    return wrapper

@country_code
def print_numbers(phone_numbers):
    for item in phone_numbers:
        print(item)

print(print_numbers(args))