

# names = ["apple", "google", "yahoo"]
# print(names[0])
# print(names.__getitem__(0))
#
# print(len(names))
# print(names.__len__())


"""................................class decorator............................................"""


# attaching init method to a class through class decorator

def demo(self, name):
    self.name = name


def attach(cls):
    cls.__init__ = demo        # Greet.__init__ = demo
    return cls


@attach         # Greet = attach(Greet)
class Greet:
    def greeting(self):
        print(f"Hello {self.name}")

f = Greet("John")   # eventhough there is no __init__ in class Greet, it has been attached through the class decorator
f.greeting()

#output - Hello John



# def log(func):
#     def wrapper(*args, **kwargs):
#         print("Logging")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def logging(cls):
#     for key, value in cls.__dict__.items():
#         if callable(value):
#             setattr(cls, key, log(value))       # add = log(add)/ sub = log(sub)/ mul = log(mul)
#     return cls