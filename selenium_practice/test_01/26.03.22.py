

import time

# def delay(spam):
#     def wrapper(*args):
#         time.sleep(5)
#         return spam(*args)
#     return wrapper
#
# @delay                   #func = delay(func)
# def func(a, b):
#     return a+b
#
# print(func(2, 3))


# def reverse(spam):
#     def wrapper(*args, **kwargs):
#         return spam(*args, **kwargs)[::-1]
#     return wrapper
#
# @reverse
# def func(l):
#     return l
#
# print(func("string"))


# def repeat(spam):
#     def inner(*args, **kwargs):
#         for i in range(3):
#             spam(*args, **kwargs)
#             time.sleep(2)
#     return inner
#
# @repeat
# def func():
#     print(10)
#
# func()


# def outer_most(n):
#     def outer(spam):
#         def inner(*args, **kwargs):
#             for i in range(n):
#                 print(spam(*args, **kwargs))
#             time.sleep(2)
#         return inner
#     return outer
#
# @outer_most(2)
# def func():
#     return "hello"
#
# func()
#
# @outer_most(3)
# def res():
#     return "world"
#
# res()
#
# @outer_most(4)
# def app():
#     return "python"
#
# app()


# def outer(spam):
#     def inner():
#         start = time.time()
#         print(start)
#         spam()
#         end = time.time()
#         print(end)
#         print(end-start)
#     return inner
#
# @outer
# def func():
#     print("hashtag")
#
# func()


# def max_calls(spam):
#     spam.count = 0
#     def wrapper(*args, **kwargs):
#         for i in range(7):
#             spam.count += 1
#             spam(*args, **kwargs)
#             if spam.count>5:
#                 raise ValueError(f"maximum calls to {spam.__name__} exceeded")
#             time.sleep(1)
#     return wrapper
#
# @max_calls
# def func():
#     print("hello")
#
# func()


l = [2,3,4,5,6]
def even():
    for i in l:
        if i%2==0:
            yield i

x = even()
print(x)
print(even())
print(list(even()))

path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Programme\File.Handling\Text_log_files\sample.txt"

def file():
    with open(path) as file:
        for line in file:
            if line.strip():
                c = len(line.split())
                yield c

l = file()
print(list(l))












































