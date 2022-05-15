
"""........https://github.com/vidyagowda159/Alpha-4/tree/master/Datatypes......."""

"""......................................string methods...................................................."""

"""https://github.com/vidyagowda159/Alpha-4/blob/master/Datatypes/collection_datatypes/string_methods.py"""

# # upper()
# s = "hello python"
# res = s.upper()
# print(res)
# print(s)
#
# # lower()
# s1 = "HELLO"
# print(s1.lower())
# print(s1)
#
# # count()
# print(s.count("l"))
# print(s.count("hello"))
# print(s.count("hello", 3))
#
# # find(), rfind()
# s = "hello python"
# print(s.find("e"))     #1
# print(s.find("o"))       #4
# print(s.find("o", 5))    #10
# print(s.find("hello"))   #0   #it will give index of first letter..
# print(s.find("d"))     #-1
#
# print(s.rfind("o"))   #10
# print(s.rfind("u"))   #-1
#
# print()
# # index(), rindex()
# s = "hello python"

# print(s.index("l"))     #2
# #print(s.index("u"))       #ValueError: substring not found
#
# print(s.rindex("l"))    #3
# print(s.rindex("py"))   #6     #will catch only first character

# print()
# # replace()
# s = "hai"
# #s[2] = "y"                             #TypeError: 'str' object does not support item assignment
# print(id(print(s.replace("i", "y"))))   #140736720420064
# print(s)                                #"hai"
# print(id(s))                            #1699856528176
#
# s = "hai how are you"
# print(s.replace("a", "z", 1))
#
# # startswith(), endswith()
# s = "hai how are you"
# print(s.startswith("hai"))
# print(s.startswith("h"))
# print(s.startswith("a", 1))
#
# print(s.endswith("h"))
# print(s.endswith("h", 0, 5))
# print()
#
# # split()
# s = "hai how are you"
#
# print(s.split())
# print(s.split("a"))
# print(s.split("a", 1))
# print(s.split(" ", 2))
#
# print()
# # join()
# s = "hai"
#
# print("-".join(s))
#
# s = "hai how are you"
# res = s.split()
# print(res)
# print(" ".join(res))
#
# print()
# # strip(), lstrip(), rstrip()
# s = "__hai__"

# print(s.strip("_"))       #hai
# print(s.lstrip("_"))      #hai__
# print(s.rstrip("_"))      #__hai

# s = "$_@_$%*_hai_!@$_"
# print(s.strip("_"))       #@__hai_@$
# print(s.strip("_$@"))       ##%*_hai_!
#
# s = "    hai    "
# print(s.strip())            #hai
#
# print()
# # boolean methods
# s = "hai"
# print(s.isalnum())       #  True
# print(s.isalpha())       #  True
# print(s.isdigit())       #  False
# print(s.islower())       #  True
# print()
#
# s = "12hai"
# print(s.isalnum())       #  False
# print(s.isalpha())       #  False
# print(s.isdigit())       #  False
# print(s.islower())       #  True
# print(s.isupper())       #  False
# print()
#
# s = "hai hello"
# print(s.isalnum())       #  False
# print(s.isalpha())       #  False
# print(s.isdigit())       #  False
#
# s = "      "
# print(s.isspace())       #  True
#
# print()
# s = "123"
# print(s.isdigit())       #  True



"""........................................list method................................"""

"""https://github.com/vidyagowda159/Alpha-4/blob/master/Datatypes/collection_datatypes/list_methods.py"""

# adding elements to the list

# append
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.append("instagram")
# print(names)

# names.append([1, 2, 3])
# print(names)

# extend
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.extend("instagram")
# print(names)
# names.extend([1, 2, 3])
# print(names)

# insert
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.insert(3, "facebook")
# print(names)

# removing elements from a list
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']

# pop
# print(names.pop(2))        #yahoo
# print(names)               #['apple', 'google', 'amazon', 'microsoft']

# print(names.pop())           #microsoft
# print(names)                 #['apple', 'google', 'yahoo', 'amazon']
# names.pop(10)                  #IndexError: pop index out of range

# remove
# names.remove("amazon")
# print(names)                 #['apple', 'google', 'yahoo', 'microsoft']
# names.remove("flipkart")
# print(names)                 #ValueError: list.remove(x): x not in list

# del

# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# del names[2:]
# print(names)
#output - ['apple', 'google']

# copy
# names = ['apple', 'google', ['yahoo', 'amazon'], 'microsoft']
# print(id(names))              #2106280072264
# print(id(names[2]))           #1492307432008
# list_ = names[::]
# print(id(list_))              #1492312771144

# l = names.copy()
# print(list_)
# print(id(l))
# print(id(l[2]))


# sorting a list
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.sort()    # ASCII
# res = sorted(names)
# print(res)                       #['amazon', 'apple', 'google', 'microsoft', 'yahoo']
# print(names)                    #['amazon', 'apple', 'google', 'microsoft', 'yahoo']

# names.sort(key=len)
# print(names)                      #['apple', 'yahoo', 'google', 'amazon', 'microsoft']
# names.sort(reverse=True)
# print(names)                      #['yahoo', 'microsoft', 'google', 'apple', 'amazon']

# using split and join
# s = "hai how are you"
# l = s.split()
# print(l)
#
# s1 = " ".join(l)
# print(s1)
#
# # using list constructor and join
# s = "hai how are you"
# l = list(s)
# print(l)
#
# s2 = "".join(l)
#..#or s2 = str().join(l)
# print(s2)                           #hai how are you


"""...................................................set Methods........................"""

"""pop, remove, discard"""

# s1 = {4,1, 2, 3, 10, 20, 30}
# print(s1.pop())
# #output - remove any character
# print(s1)
# #output - remaining set after removing any character
#
# # s1.remove(100)
# # print(s1)
# #output - KeyError
#
# print(s1.discard(100))
# #output - None
# print(s1)
# #output - remaining set after removing any character


"""isdisjoint()"""
# s1 = {1, 2, 3}
# s2 = {4, 5, 6, 2}
# print(s1.isdisjoint(s2))
#output - False


"""issuperset()"""
# a = {1, 2, 3, 4, 5, 6, 7, 8}
# b = {1, 2, 3}

# print(a.issuperset(b))
#output - True
# print(b.issuperset(a))
#output - False
# print(b.issubset(a))
#output - True