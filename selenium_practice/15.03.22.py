

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

from time import sleep

# driver.get("http://www.tutorialsninja.com/demo/")
# sleep(2)
# driver.find_element_by_xpath("//a[@href='http://tutorialsninja.com/demo/index.php?route=product/category&path=24']").click()
# sleep(2)
# driver.find_element_by_xpath("//a[text()='iPhone']").click()
# sleep(2)
# driver.find_element_by_xpath("//img[@src='http://tutorialsninja.com/demo/image/cache/catalog/demo/iphone_1-228x228.jpg']").click()
# sleep(2)
# x = driver.find_element_by_xpath("//button[@title='Next (Right arrow key)']")
#
# for i in range(5):
#     x.click()
#     sleep(2)



# driver.get("https://www.ajio.com/shop/")
#
# driver.find_by_element_xpath("//a[@href='/shop/men'']").click()
# driver




#.............................................................................

# driver.get("https://ajio.com/s/bedsheet-4203-72291")
# sleep(5)
# items = driver.find_elements_by_xpath("//div[@class='nameCls']")
# prices = driver.find_elements_by_xpath("//span[@class='price  ']")
#
# i1 = [item.text for item in items]
# p1 = [item.text for item in prices]
#
# d = {items:prices for items, prices in zip(i1,p1)}
# print(d)
# z = sorted(d.items(), key=lambda i: i[-1])
# print(z)
# print(z[-1][-1][1:])
# print(z[0][-1][1:])









