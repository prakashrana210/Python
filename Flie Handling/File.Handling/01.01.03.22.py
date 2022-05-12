
#practice class qns - file handling - 02.20.02.22.reading.files
#practice class qns - file handling - 03.20.02.22.jason.file.handling
#practice class qns - file handling - 04.20.02.22.pickle.file.handling
#practice class qns - file handling - 06.20.02.22.writing.files

from collections import defaultdict, Counter
path = r"/Flie Handling\File.Handling\Text_log_files\sample.txt"

""" line number and line in the file """

#using enumerate()

# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)


""" count number of words in the file """

#.a

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             count += 1
# print(count)

#.b

# with open(path) as file:
#     count = 0
#     for line in file:
#         #count += len(line.split())
#                 #or
#         #words = line.split()
#         #count += len(words)
#
# print(count)


""" reading a file in reversed order """

# with open(path) as file:
#     for line in reversed(list(file)):                   #doubt why we are using list
#         print(line)


""" count number of whitespaces """#..............................................


""" count the number of words starting with vowels """

#with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
# print(count)


""" word and its count pair """

#.......................................#doubt.....this is not working... why
# with open(path) as file:
#     d = {}
#     for line in file:
#         for word in set(line.split()):
#             d[word] = line.split().count(word)
# print(d)

# with open(path) as file:
#     d = {}
#     for line in file:
#         for word in line.split():
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
# print(d)

#output - {'hello': 8, 'world': 6, 'universe': 2, 'welcome': 2, 'to': 2, 'python': 5, 'programming': 1, 'in': 1, 'is': 3, 'fun': 2, 'java': 1, 'easy': 1}


""" list of ip address from access-log.txt file """

path = r"/Flie Handling\File.Handling\Text_log_files\access-log.txt"

# with open(path) as file:
#     for line in file:
#         if line.strip():
#             print(line.split()[0])

""" create a dictionary of ip addresses and their count"""

# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             if line.split()[0] not in d:
#                 d[line.split()[0]] = 1
#             else:
#                 d[line.split()[0]] += 1
# print(d)


""" print nth line from the file """

#from itertools import islice
# n = 3
# with open(path) as file:
#     res = islice(file, n-1, n)
#     print(list(res))                             #doubt why we are using list

#we could this qns through two other methods
#through enumerate
#through count


""" to print first n lines """#.....................................................



""" last n lines """
from itertools import islice
n = 3

#through islice

#with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     res = list(islice(file, count-n, count))
# print(res)


#through deque

# from collections import deque
# n = 3
# with open(path) as file:
#     for line in file:
#         res = list(deque(file, n))
#         print(res)

#.............................................................................................................

#practice class qns - file handling - 03.20.02.22.jason.file.handling


# import json
# a = {"hai": 3, "hello": 4}

# b = json.dumps(a)
# print(b)
# print(type(b))

#output - {"hai": 3, "hello": 4}
#          <class 'str'>

# c = json.loads(b)
# print(c)
# print(type(c))

#output - {'hai': 3, 'hello': 4}
#          <class 'dict'>


#........................................................

# import json
#
# a = True
# print(type(a))
# #output - <class 'bool'>
#
# b = json.dumps(a)
# print(b)
# print(type(b))

#output - true
#         <class 'str'>

# c = json.loads(b)
# print(c)
# print(type(c))

#output - True
#         <class 'bool'>

#................................................

import json

# a = {"a": 1, "b": 2, "c": 3}
#
# with open("sample.json", "a") as file:
#     print(json.dump(a, file))

#output - None

# with open("sample.json") as file:
#     print(json.load(file))

#output - {'a': 1, 'b': 2, 'c': 3}


#..............................................................................................................

#practice class qns - file handling - 04.20.02.22.pickle.file.handling

import pickle

# a = "hai"
#
# b = pickle.dumps(a)
# print(b)
# print(type(b))

#output - None
#         b'\x80\x03X\x03\x00\x00\x00haiq\x00.'
#         <class 'bytes'>

print()

# c = pickle.loads(b)
# print(c)
# print(type(c))

#output - hai
#         <class 'str'>



#.............................................................................................................
import os
print(os.getcwd())
path = r"/Flie Handling\File.Handling\Text_log_files\sample.txt"
print(os.getcwd())

# with open(path) as file:
#     data = file.read()                     #read complete file
#     print(data)
#     print()
#     print(file.tell())                      #gives the position of the cursor
#     file.seek(0)
#     print()
#     print(file.read(15))                    #give 10 character from the file
#     print()
#     print(file.read(5))                     #it will give the next charchter after the previous output
#     print()
#     print(file.read())                      #it will read all the left character in the file
#     print()
#     print(file.tell())   #position 208
#     file.seek(0)                           #since cusror is at the last spot now, to read again we need do seek(0)
#     print(file.tell())   #position 0
#     print(file.readline(2))                 #read entire line
#     print()
#     print(file.readline(20))               #sine after the previous step cursone is at the last position
#                                            #of first line so now in this step it will give character from next line


# with open(path) as file:
#     print(file.readlines())                #read the complete file in the form of list and each line as
                                             # string in the list

#..........................................................................................................

#practice class qns - file handling - 06.20.02.22.writing.files

#in this we are creatinig and appending a file, (if file already exist, it will append with the content
#which is already present there)

#f_path is the path, in which system is going to create a new file and then if we write in append mode then
#it will simply append in the file

#the new file name is created by the system as path + f_path

# f_path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txtfile1.txt"
#
# with open(path + "sample.txtfile1", "a") as file:
#     print(file.writelines(["hai\n", "hello\n", "python"]))

# selenium_practice

path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txt"
path_f = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txtfile1.txt"

with open(path, 'r') as file1, open(path_f, 'w') as file2:
    for line in file1:
        file2.write(line)