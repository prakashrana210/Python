
# from selenium import webdriver
# driver = webdriver.Chrome("chromedriver")
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# action = ActionChains(driver)
# driver.implicitly_wait(10)
# driver.get("https://www.google.com/")
# action.move_to_element(driver.find_element_by_xpath('//a[@aria-label="Google apps"]')).click().perform()
# sleep(2)
# action.move_to_element(driver.find_element_by_xpath('//body[@jsmodel="hspDDf"]')).click().perform()# driver.close()

# popup = driver.switch_to.alert
# popup.accept()
# popup.dismiss()
#
# driver.find_element_by_xpath("...").send_keys("..path_of_the_file_or_image..")
#
# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath("...")).perform()
# action.move_to_element(driver.find_element_by_xpath(("..........)"))).click().perform()
#
# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)
# action.context_click(driver.find_element_by_xpath("..")).perform()
#
# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)
# action.double_click(driver.find_element_by_xpath("..")).perform()
#
# handle = driver.window_handles[1]
# driver.switch_to.window(handle)
# #..or.. driver.switch_to.window(driver.window_handles[1])
#
# driver.switch_to.frame(driver.find_element_by_xpath(("...")))


#     # from selenium.webdriver.common.by import By
#     # from selenium.webdriver.support import expected_conditions
#     # from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
# WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "...")))


"""...........................highest price.............................................................."""


# from selenium import webdriver
# driver = webdriver.Chrome("chromedriver")
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element_by_xpath('//button[@id="details-button"]').click()
# driver.find_element_by_id("proceed-link").click()
#
# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath('//ul[@class="top-menu"]//a[@href="/computers"]')).perform()
# action.move_to_element(driver.find_element_by_xpath('//ul[@class="top-menu"]//a[@href="/accessories"]')).click().perform()
#
# #............#driver.find_element_by_xpath('//a[contains(text(),"TCP Instructor Led Training")]/../../..//input[@value="Add to cart"]').click()
#
# prices = driver.find_elements_by_xpath('//span[@class="price actual-price"]')
# pri = []
# for price in prices:
#     b = price.text[:-3]
#     pri.append(b)
# res = sorted(pri)
# print(res[-1])

#output = 9000

# a = "hellFGHHo3$453"
# print("".join(sorted(a)))



"""............................................copy, shallow copy, deepcopy.............................."""


# l = [2,3,[4,5],6]
# d = l
# d[2][0]=2
# d.append(7)
# print("l :", l)
# print("d :", d)
#
# #output -
# l : [2, 3, [2, 5], 6, 7]
# d : [2, 3, [2, 5], 6, 7]
# print()
#
# l = [2,3,[4,5],6]
# import copy
# d = copy.copy(l)
# d[2][0]=2
# d.append(7)
# print("l :", l)
# print("d :", d)
#
# #output -
# l : [2, 3, [2, 5], 6]
# d : [2, 3, [2, 5], 6, 7]
#
# print()
#
# l = [2,3,[4,5],6]
# import copy
# d = copy.deepcopy(l)
# d[2][0]=2
# d.append(7)
# print("l :", l)
# print("d :", d)
#
# #output -
# l : [2, 3, [4, 5], 6]
# d : [2, 3, [2, 5], 6, 7]


"""....................................pattern priniting........................................................"""


# for i in range(5,1,-1):
#     print(f'{"* " * i:^10}')
# for i in range(1,6):
#     print(f'{"* " * i:^10}')
#
# for i in range(1,6):
#     print("* " * i)
# for i in range(5,0,-1):
#     print("* " * i)
#
# for i in range(1,6):
#     print(f'{"* " * i:>10}')
# for i in range(5,0,-1):
#     print(f'{"* " * i:>10}')


# res = " "
# for i in range(1,6):
#     res += str(i)
#     print(res)

# res = " "
# for i in range(5,0,-1):
#     res += str(i)
#     print(res)

# res = " "
# for i in range(1, 6):
#     res += str(i)
#     print(f"{res}")

# res = " "
# for i in range(5,0,-1):
#     res += str(i)
#     print(res[1:])


# res = " "
# for i in range(ord('a'), ord('f')):
#     res += chr(i)
#     print(res)
#  a
#  ab
#  abc
#  abcd
#  abcde


# res = " "
# for i in range(ord('a'), ord('f')):
#     res += chr(i)
#     print(f"{res[1:]:>6}")
#      a
#     ab
#    abc
#   abcd
#  abcde


# for row in range(ord('a'), ord('e')+1):
#     for col in range(ord('a'), row+1):
#         print(chr(col), end=" ")
#     print()
# a
# a b
# a b c
# a b c d
# a b c d e


# x = " "
# for row in range(ord('a'), ord('e')+1):
#     x += chr(row) + " "
#     print(x)
#  a
#  a b
#  a b c
#  a b c d
#  a b c d e


# for row in range(ord('a'), ord('e')+1):
#     for col in range(ord('a'), row+1):
#         print(chr(col), end=" ")
#     print()
# a
# a b
# a b c
# a b c d
# a b c d e

# import re
# a = "9000.00"
# res = re.findall(r'\d+'{4}, a)


from selenium import webdriver
driver = webdriver.Chrome("chromedriver")
# from selenium.webdriver.common.action_chains import ActionChains
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/")
driver.find_element_by_xpath('//button[@id="details-button"]').click()
driver.find_element_by_id("proceed-link").click()
driver.find_element_by_xpath('//ul[@class="top-menu"]//a[@href="/books"]').click()
cart = driver.find_elements_by_xpath('//input[@value="Add to cart"]')
for i in cart:
    i.click()
    print(i.text)
# driver.find_element_by_xpath('//li[@id="topcartlink"]//span[@class="cart-label"]').click()

