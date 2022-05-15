
# notes for csv file
# https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/#:~:text=Reading%20from%20CSV%20file&text=At%20first%2C%20the%20CSV%20file,in%20the%20specified%20CSV%20document.


# l = ["we", "are", "here"]
# g = "leonardo bhai"
# p = "rocky bhai"
# q = ["hello", "we", "are", "here"]
# d = ("ab", "cde", 2, 3)
# e = {"fgh", "ijk", 4, 5}
# k = {"zx":2, "fg":4}
# m = 4
# n = 7
#
# f = open('sample.txt', "a")
# f.writelines(l)
# f.writelines(g)
# f.writelines(k)
# #f.writelines(d)                       write() argument must be str, not int
# # f.writelines(e)                      write() argument must be str, not int
# # f.write(q)                           write() argument must be str, not list
# # f.write(m)                           write() argument must be str, not list
# # f.writelines(n)                      'int' object is not iterable


path = r"/Flie Handling\File.Handling\Text_log_files\sample.txt"
# l = ["we", "are", "here"]
# with open(path, "a") as file:
#     for i in l:
#         file.writelines(i)


# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)


# with open(path) as file:
#     d = file.readline()
#     for i in d:
#         print(i, end="")


# with open(path) as file:
#     d = file.readlines()
#     for i in d:
#         print(i)


# with open(path) as file:
#     file.seek(7)
#     print(file.tell())
#     print(file.read())
#     print(file.seek(255))
#     print(file.read())
#     print(file.tell())



#csv file

# with open(path_) as csv_file:
#     read_obj = csv.reader(csv_file)
#     for word in read_obj:
#         print(word)
#
# with open(path_) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     for word in read_obj:
#         print(word)

# path1 = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txt"
# path2=

# with open("sample.txt", "r") as file1, open("sample.txtfile1.txt", "a") as file2:
#     for line in file1:
#         print(line)
#         words = line.split()
#         print(words)


import os
# #with open("sample.txt", "r") as file1, open("sample.txtfile1.txt", "a") as file2:
#     for line in file1:
#         if line == 2:
#             file2.write(line)


with open(path) as file:


