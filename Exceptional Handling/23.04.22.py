
#....github alpha 4

# try - except

# default except block
# a = 1
# b = 1
#
# try:
#     print("in try block")
#     z = a / b
#     print(z)
#
# except:
#     print("in except block")


# a = 2
# b = 0
# try:
#     print("in try block")
#     z = a/b
#     print(z)
# except ZeroDivisionError:
#     print("in except block")



a = 1
b = 0
try:
    z=a/b
    print(z)
except ZeroDivisionError:
    print(f"{a} is not divisble by {b}")















