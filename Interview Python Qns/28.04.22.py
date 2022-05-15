
# Squire Boat

arr = [1,2,3,4,6,7,8]
# for i in range(len(arr)-1):
#     if arr[i] + 1 not in arr:
#         print(arr[i]+1)


#................................................................................not done
# def func(lst):
#     for i,v in enumerate(lst, start=1):
#         if v in lst:
#             print(f"if v = {v}, then index = {i}")
#         #     lst.insert(i+1, v+1)
#         #     #return (f" the number {v+1} is not present so it is suitable for {v+1} position and it should place after 4 and before 6")
#         # else:
#         #     print(f"if v = {v}, then index = {i}")
#     print(lst)
# func(arr)



def func(lst, n):
    for i,v in enumerate(lst, start=1):
        if n in lst and n == v:
            return (f"index of {n} is {i}")
        elif n not in lst:
            return (f"suitable postion of {n} is between {n-1} and {n+1}")

# print(func(arr, 3))
# print(func(arr, 5))
# print(func(arr, 7))

    # index of 3 is 3
    # suitable postion of 5 is between 4 and 6
    # index of 7 is 6


# 5) Write a function where
#  i/p=56 , o/p should be 2536
# 6)difference between shallow and deep copy

s = 567
# l = str(56)
def func(a):
    for i in str(a):
        if True:
            b = str(a).replace(i, str(int(i)*int(i)))
            k = int(b)
    print(int(k))
    print(type(b))
    print(type(k))
func(s)


# print(s)
# print(l)
# a  = 24
# print(str(24))
# print(str(int(l)))


#..............................................wrong done
# s = 56
# l = str(56)
# res = " "
# for i in l:
#     res += l.replace(i, str(int(i)*int(i)))
# print(res)


# a = "right"
# print(a.replace("r", "m"))
# print(a)


# a = [2,3,4]
# b = a.copy()
# print(b)

# a = [2,3,4,[4,5],8]
# b = a.copy()
# print(b)

# a = "right"
# print(a.replace("r", "l"))
# b = a.replace("r", "l")
# print(b)

#...............................................correct
# s = 56
# l = str(56)
# res = " "
# for i in l:
#     res += str(int(i)**2)
# print(res)


# s = 56
# l = str(56)
# res = []
# for i in l:
#     res.append(int(i)**2)
# print("".join(res))


