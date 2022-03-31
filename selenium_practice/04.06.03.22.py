
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")

# from selenium.webdriver import Chrome
# driver = Chrome("./chromedriver")

from time import sleep
#or import time

#..........................................................................................

# driver.get("file:///C:/Users/Admin/Downloads/xpath.html")
#
# sleep(5)
#
# driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("Shiv")
# sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("Prakash")
# sleep(2)
# driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("test yantra")
# sleep(2)
# driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("Bengalore")

#..........................................................................................demo


#driver.get("file:///C:/Users/Admin/Downloads/demo.html")

#...................................

# driver.find_element_by_xpath("//input[@type='checkbox']").click()

# .....pic(03.03.22..11:59 pm)
# a = driver.find_elements_by_xpath("//input[@type='checkbox']")
#
# for i in range(len(a)-1, -1, -1):
#     a[i].click()
#     sleep(2)

#....................................

#...(03.03.33....12:22)

# driver.get("https://www.python.org/")
#
# links = driver.find_elements_by_xpath("//a")
# data = []
#
# for item in links:
#     link_text = item.text.strip()
#     url = item.get_attribute("href")
#     if "python" in link_text:
#         data.append((link_text, url))
#         print(len(data))
#         print(data[0])

#output -
# 1
# 2
# 3

# 1
# ('docs.python.org', 'https://docs.python.org/')
# 2
# ('docs.python.org', 'https://docs.python.org/')
# 3
# ('docs.python.org', 'https://docs.python.org/')

#..............................




