

#alpha-4 , OOPs

# class Employee:
#     fname = "steve"         # class variables
#     lname = "jobs"
#
#     def __init__(self, age, salary):
#         self.age = age          # object/instance variables
#         self.salary = salary
#
#
# emp1 = Employee(20, 30000)
# emp2 = Employee(30, 40000)
#
# # modification w.r.t objects
# emp1.fname = "Einstien"
# print(emp1.fname)   # Einstien
# print(emp2.fname)   # steve
# print(Employee.fname)   # steve



# shares = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20}
#
# def func(item):
#     if item[1] > 40:
#         return item
#
# res = list(filter(func, shares.items()))
# print(res)
#
# print(sorted(res, key=lambda item: item[-1]))


#group the sorted items
# l = ["tea", "eat", "silent", "hello", "listen", "ate"]
# d = {}
# for i in l:
#     key = "".join(sorted(i))
#     if key not in d:
#         d[key] = [i]
#     d[key] += [i]
#
# print(d)


# l = ["tea", "eat", "silent", "hello", "listen", "ate"]
# from collections import defaultdict
# dd = defaultdict(list)
# for i in l:
#     key = "".join(sorted(i))
#     dd[key] += [i]
#
# print(dd)

#....static method

class Calculator:
    a = 10
    b = 4

    def add(self):
        # print(self)
        # print(Calculator)
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


calci1 = Calculator()

# calling add() using object
# print(calci1.add())
# calling add() using class
# print(Calculator.add(calci1))
# print(calci1.add())


#........................................................................................class method

#..It does not depend upon the creation of object. or it does not require any object.

# class Employee:
#     name = "John"
#     id = 10
#
#     @classmethod
#     def display(cls):
#         print(cls.name, cls.id)
#
#     def spam(self):
#         print("in spam method")


# e = Employee()
# e.display()       #john 10
# Employee.display()             #john 10
# e.spam()              #in spam method
#Employee.spam(Employee())           #in spam method



# class func:
#     a = 4
#
#     @classmethod
#     def func_(cls, b):
#         cls.a = b
#
# x = func()
# x.func_(6)
# print(x.a)



# class sample_:
#     def __init__(self, date, month, year):
#         self.date = date
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def data(cls, date_):
#         date, month, year = date_.split("-")
#         object_ = cls(date, month, year)
#         return object_
#
# x = sample_.data("20-05-22")
# print(x.date)
# print(x.month)
# print(x.year)


# from time import sleep
#
# def outer(n):
#     def spam(func):
#         def wrapper(*args, **kwargs):
#             sleep(n)
#             print(func(*args, **kwargs))
#         return wrapper
#     return spam
#
# @outer(6)
# def func(a):
#     return 3, a
#
# func(4)


# log decorator

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log        # print_ = log(print_)      : func -> print_, print_ - wrapper
# def print_():
#     print("This is main function")

# print_()



# def count_(func):
#     def wrapper(*args, **kwargs):
#         print(f'total number of arguments: {len(args), len(kwargs)}')
#         return func(*args, **kwargs)
#     return wrapper
#
# @count_
# def display(a, b):
#     return a, b
#
# display(1, 2)


# from time import time
#
# def outer(spam):
#     def wrapper(*args, **kwargs):
#         start = time()
#         res = spam(*args, **kwargs)
#         end = time()
#         return f"execution time: {end-start}", f"output of display: {res}"
#     return wrapper
#
# @outer
# def display():
#     return "in display"
#
# print(display())









