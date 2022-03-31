from selenium import webdriver

# driver = webdriver.Chrome("./Chromedriver")
#
# driver.get("http://demowebshop.tricentis.com")
# driver.maximize_window()

from time import sleep

#launches a new chrome browser
driver = webdriver.Chrome("./Chromedriver")
driver.maximize_window()


# driver.get("http://services.smartbear.com/samples/TestComplete14/smartstore/")
driver.get("http://demowebshop.tricentis.com/books")
sleep(4)

driver.find_element_by_xpath("//a[text()='Fiction']/../../input[@value='Add to cart']").click()
#element = driver.find_elements_by_xpath("//img")

# images = driver.find_elements_by_xpath("//img")
#
# for image in images:
#     print(image.get_attribute("alt"))
#     sleep(1)

