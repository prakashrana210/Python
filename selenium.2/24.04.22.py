
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.select import Select

# #driver.get("https://google.com")
#
# driver.find_element_by_xpath('//div[@class="gb_Se"]/div/div/div/a').click()
#
# action = driver.A
# driver.find_element_by_xpath('//body[@jsmodel="hspDDf"]').click()



# driver.get("file:///C:/Users/Admin/Downloads/demo.html")
# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
# for i in checkboxes:
#     print(i.click())
#     sleep(1)



#.........................................................................................not working
# driver.get("file:///C:/Users/Admin/Downloads/demo.html")
# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
#
# select = Select(checkboxes)
#
# all_options = select.options
#
# for i in all_options[::-1]:
#     select.select_by_visible_text(i.text)


#..............................................................................not working
# driver.get("file:///C:/Users/Admin/Downloads/demo.html")
# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
#
# for i in checkboxes[::-1]:
#     i.click()
#     #break




#...................................................................
