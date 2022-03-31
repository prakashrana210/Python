


#................................................................................basic programme

from selenium.webdriver import Chrome

from time import sleep


#launches a new chrome browser

driver = Chrome("./chromedriver")
driver.maximize_window()

#navigate to demowebshop

driver.get("http://demowebshop.tricentis.com/books")



#driver.get("fileC:\Users\Admin\Downloads\xpath.html")

# current_title = driver.title
#
# url = driver.current_url
#
# print(current_title)
# print(url)
#
# driver.minimize_window()
# sleep(2)
#
# driver.maximize_window()
# sleep(2)
#
# driver.close()

#................................................................................

# driver.find_element_by_link_text("register").click()
#
# driver.find_element_by_class_name()

# driver.find_element_by_xpath()

#................................................................................

#driver.find_element_by_css_selector("a[class='ico-register']").click()
# sleep(2)
# driver.find_element_by_css_selector("a[class='ico-register']").click()
#
# driver.find_element_by_css_selector()

driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@value='Add to cart']").click()

#driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys(first_keys("firstname"))

driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@value='Add to cart']").click()

driver.find_elements_by_name("book").click()