


from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

#launches a chrome browser

#................................................not working
# driver.get("https://www.makemytrip.com/")
#
# driver.find_element_by_xpath("//span[@class='tabsCircle appendRight5']//span").click()
#...................................................

from time import sleep

#...........................................................

driver.get("https://www.facebook.com/")

driver.find_element_by_xpath("//input[@autofocus='1']").send_keys("prakashrana007")
sleep(2)
driver.find_element_by_xpath("//input[@id='pass']").send_keys("prakash@25")
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()

#...........................................................

driver.get("https://web.whatsapp.com/")

""" 11. Write program to read a random line in a file. (ex. 50, 65, 78th line) """






