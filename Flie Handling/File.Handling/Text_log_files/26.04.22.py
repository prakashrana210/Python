
# notes for csv file
# https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/#:~:text=Reading%20from%20CSV%20file&text=At%20first%2C%20the%20CSV%20file,in%20the%20specified%20CSV%20document.



import os
from itertools import islice

path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txt"
path_f = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\sample.txt.2"

# with open(path, 'r') as file, open(path_f, 'w') as file2:
#     for line in file:
#         file2.write(line)


# with open(path, 'r') as file, open(path_f, 'w') as file2:
#     for line in file:
#         file2.writelines(line)



#................................................................

import csv
path = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\access-log.txt"
path_f = r"C:\Users\Admin\PycharmProjects\shiv_prakash\Flie Handling\File.Handling\Text_log_files\access.log.txt2"

# with open(path, "r") as file:
#     r_obj = csv.reader(file)
#     for line in r_obj:
#         print(line)
#         print(type(line))


# with open(path, "r") as file, open(path_f, "w")as file2:
#     r_obj = csv.reader(file)
#     for line in r_obj:
#         csvwriter = csv.writer(file2)
#         csvwriter.writerows(line)
#         print(type(line))



# with open(path_f, "r") as file, open(path, "w") as file2:
#     r_obj = csv.reader(file)
#     for line in r_obj:
#         csvwriter = csv.writer(file2)
#         csvwriter.writerow(line)

with open(path) as file, open(path_f, "w") as file2:
    for line in file:
        file2.write(line)











#.........if we want to write the list of string in the file, then use writelines

# l = ["hello", "duniya"]
# with open(path_f, "a") as file:
#     file.writelines(l)
#     file.write("\n")  #if we want to in


#.........if we want to write the string in the file

s = "earth is a best place"
with open(path_f, 'a') as file:
    file.writelines("\n")
    file.writelines(s)

s = "earth is a best place"
with open(path_f, "a") as file:
    file.write("\n")
    file.write(s)
