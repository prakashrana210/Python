

# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# from time import sleep


"""not working -- click on google and click on youtube"""

# driver.get("https://www.google.com/")
# sleep(5)
# handle = driver.window_handles
# driver.switch_to.window(handle[1])
# driver.find_element_by_xpath('//button[@aria-label="No thanks"]').click()
# handle = driver.window_handles
# driver.switch_to.window(handle[1])
# sleep(5)
# driver.find_element_by_class_name("gLFyf gsfi").send_keys("rahul khadoliya")


# driver.get("https://www.google.com/")
# sleep(10)
# popup = driver.switch_to.alert
# popup.dismiss()
# driver.find_element_by_class_name("gLFyf gsfi").send_keys("rahul khadoliya")



"""working-- write name in the box"""

# driver.get("file:///C:/Users/Admin/Downloads/demo.html")
# names = driver.find_elements_by_class_name("first_row")
# count = 0
# for i in names:
#     count += 1
#     i.send_keys("rahul")
# print(count)


s = 's123'
print(int(s[1:]))





