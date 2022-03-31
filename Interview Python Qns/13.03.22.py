
#.................................................................................................................
""" 36 Sum all the numbers in the below string. """

#.a

s = "Sony12India567Pvt2ltd"

# add = 0
# for i in s:
#     if "0"<=i<="9":
#         add += int(i)
# print(add)

#ooutput - 23

#.b

# s = "Sony12India567Pvt2ltd"
# add = 0
# for i in s:
#     if i.isdigit():
#         add += int(i)
# print(add)

#output - 23

#.........................................................................
""" 37 Write a program to sum all the numbers in below string. """



""" 38 Print all the numbers in the below list """
# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isdigit():        #"0"<=i<="9"
#         print(i, end="")

#output - 12323


""" 39 Program to print the number of occurrences of characters in a String without using inbuilt functions. """

# s = 'helloworld'
# for i in set(s):
#     print(i, s.count(i), sep="-")


""" 40 Program to print only the repeated characters and count of the same. """

# s = 'helloworld'
# for i in s:
#     if s.count(i)>1:
#         print(i, end=" ")

""" 41 Write a program to get alternate characters of a string in list format. """

# s = 'hello world welcome to python'
# res = []
# for i in range(len(s)):
#     if i%2 == 0:
#         res.append(s[i])
# print(res)



""" 42 Write a program to get square of list of number's using lambda function . """

# l = [2,3,4,5,6]
# res = lambda a: a**2
# print(res(l))


""" 43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other. """

def func(a, b):
    if sorted(a) == sorted(b):
        print(a, b, "is anagram")
    else:
        print(a, b, "is not anagram")
func("tea", "eat")



""" 44 Write a program to iterate through list and build a new list, only if the items of the list has even number of 
characters."""

names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

l = [i for i in names if len(i)%2==0]
print(l)



""" 45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even 
number of characters. """

names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

# l = {v:len(v) for i,v in enumerate(names) if len(v)%2==0}
# print(l)



""" 46 Write a program which squares the numbers in a list using map object """

# f = [2,3,4,5,6]
# def func():
#     for i in l:
#         print(i**2)



""" 47 Count number of lines in a file without loading the file to the memory """

# path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Programme\File.Handling\Text_log_files\sample.txt"
# with open(path) as file:
#


""" 48 Printing line and line no's """



""" 49 Write a Program to print the sum of entire list and sum of only internal list """

# l = [[1,2,3],[4,5,6],[7,8,9]]
# entire_sum = 0
#
# for i in l:
#     inner_sum = 0
#     for j in i:
#         inner_sum += j
#     entire_sum += int(i)
# print(inner_sum)
# print(entire_sum)




