

# names = ["bob", "steve", "alex", "maya", "john"]
# def odd_length():
#     for i in names:
#         if len(i)%2!=0:
#             yield (i)
#
# x = odd_length()
# print(next(x))
# print(next(x))

# print(list(x))

#............................................................................


# def disp(a,b):
#     yield a
#     yield b
# x,y = disp(10,20)
# print(x)
# print(y)

#output -
# 10
# 20

# def disp(a,b):
#     yield a
#     yield b
# x = disp(10,20)
# print(x)

#output - <generator object disp at 0x000001C44D5E5A48>

# def disp(a):
#     yield a
# x = disp(10)
# print(x)

#output - <generator object disp at 0x000001A03AA55A48>


