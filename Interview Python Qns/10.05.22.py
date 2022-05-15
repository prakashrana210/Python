
"""..............................open google and seacrh........................"""

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
driver.implicitly_wait(2)
# from time import sleep
driver.get("https://google.com")
driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys("prakash rana")
# sleep(2)
driver.find_element_by_xpath('//input[@value="Google Search"]').click()

"""..............................all 0 should be at the last......................."""

# l = [-1,0,2,3,4,0,2,0]
# p = sorted(l, reverse = True, key=lambda i: abs(i))

# print(p)


"""........................count without built in method............................"""

# s = "abbcccddddeeeee"
# from collections import defaultdict
# dd = defaultdict(int)
# for i in s:
#     dd[i] += 1
# print(dd)


"""...............................normal copy......................................."""

# l = [2,3,4,5,[4,5]]     #....copy everything, nested as well as outer
# d = l
# d.append(6)
# d[4][1] = 6
# print(d)
# print(l)

#output -
# [2, 3, 4, 5, [4, 6], 6]
# [2, 3, 4, 5, [4, 6], 6]

"""...............................shallow copy......................................"""

# import copy
# l = [2,3,4,5,[4,5]]        #...........copy in only nested list not outer list
# d = copy.copy(l)
# d.append(6)
# d[4][1] = 6
# print("l :", l)
# print("d :", d)
#
# #output
# l : [2, 3, 4, 5, [4, 6]]
# d : [2, 3, 4, 5, [4, 6], 6]



"""..................................deepcopy.........................................."""


# import copy
# l = [2,3,4,5,[4,5]]       #...........do not copy, neither in nested nor in outer
# d = copy.deepcopy(l)
# d.append(6)
# d[4][1] = 6
# print("l :", l)
# print("d :", d)
#
# #output
# l : [2, 3, 4, 5, [4, 5]]
# d : [2, 3, 4, 5, [4, 6], 6]



# s = "abbcccddddeeeee"
# count = 1
# d = {}
# for i in s:
#     count += 1
#     if count == 1:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)



