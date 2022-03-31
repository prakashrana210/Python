
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

# from selenium.webdriver import Chrome
#
# driver = Chrome("./chromedriver")


from time import sleep

#launches a new chrome browser


#driver.maximize_window()

#navigate to demowebshop

#driver.get("//demowebshop.tricentis.com/books")

#driver.get(file:///Users\Admin\Downloads\xpath.html")

#current_title = driver.title

#url = driver.current_title

#print(current_title)

#print(url)

# driver.minimize_window()
# sleep(2)
#
# driver.maximize_window()
# sleep(2)
#
# driver.close()
#
# driver.quit()

sleep(5)

#driver.find_element_by_link_text("Computing and Internet").click()

#driver.find_elements_by_xpath("//a[text()='Computing and Internet']").click()

# driver.find_element_by_partial_link_text('Computing and Internet').click()
#
# driver.find_element_by_partial_link_text('Computing a').click()

#driver.find_element_by_css_selector("a[text()='Computing and Internet']").click()

#driver.find_element_by_partial_link_text("//a[text()='Computing a']").click()

#driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@value='Add to cart']").click()



driver.get("file:///C:/Users/Admin/Downloads/xpath.html")
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("Shiv")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("Prakash")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("test yantra")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("Bengalore")
sleep(2)


