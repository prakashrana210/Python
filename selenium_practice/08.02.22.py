


#validate the prices of all the gadets against the expected price

# from selenium import webdriver
# from time import sleep

# from selenium.webdriver import Chrome
#
# driver = Chrome("./chromedriver")
#
#
# driver = webdriver.Chrome("./chromedriver")
#
# driver.get("http://demowebshoptricentis.com/")
#
# sleep(5)

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver import Chrome
# from time import sleep

# from selenium.webdriver import Chrome
#
# driver = Chrome("./chromedriver")
from time import sleep

#launches a new chrome browser

#driver.maximize_window()

#navigate to demowebshop

#driver.get("//demowebshop.tricent

# from selenium.webdriver import Chrome
#
# driver = Chrome("./chromedriver")

#
# from time import sleep
#
# #launches a new chrome browser
#
#
# #driver.maximize_window()
#
# #navigate to demowebshop
#
# #driver.get("//demowebshop.tricent

from selenium.webdriver import Chrome

driver = Chrome("./chromedriver")

from time import sleep

#launches a new chrome browser

driver.maximize_window()

#navigate to demowebshop

driver.get("//demowebshop.tricentis.com/books")

driver.find_element_by_link_text("Computing and Internet").click()

