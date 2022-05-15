
# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# from time import sleep



""".............................................................................popup alert...."""

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element_by_id("name").send_keys("prakash")
# sleep(2)
# driver.find_element_by_id("alertbtn").click()
# sleep(2)
# popup = driver.switch_to.alert
# #or we can use -- popup = driver.switch_to_alert()
# sleep(2)
# assert "prakash" in popup.text
# popup.accept()

#.. popup.dismiss() ..is used if we want to select the cancel option in the popup



"""......................................................................................Upload..."""

# driver.get("https://the-internet.herokuapp.com/upload")
# sleep(2)
# # driver.find_element_by_id("file-upload").send_keys("D:\\Selenium\\3.upload.png")
# button = driver.find_element_by_id("file-submit")
# assert "upload" in button.text
# print("upload file")
# button.click()

#.. to upload the file or image we need to give command send_keys and inside the send_keys we need to give file path





"""......................................................................................Explicit.Wait..."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# driver.implicitly_wait(20)
# # driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
# driver.get("https://chercher.tech/practice/implicit-wait-example")
# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
# for i in checkboxes:
#     i.click()

# WebDriverWait(driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "......")))


"""...........................................................................................Mouse Hover.."""

""".......................................................................................working..."""

# from selenium.webdriver.common.action_chains import ActionChains
#
# driver.get("https://www.myntra.com/")
#
# action = ActionChains(driver)
#
# driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys("prakash")
# sleep(2)
#
# profile = driver.find_element_by_xpath("//span[text()='Profile']")
# action.move_to_element(profile).perform()
# sleep(5)
# login = driver.find_element_by_xpath("//a[text()='login / Signup']")
# action.move_to_element(login).click().perform()


"""..............................................................................not working..."""

# from selenium.webdriver.common.action_chains import ActionChains

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()

# driver.implicitly_wait(20)
#
# action = ActionChains(driver)

# action.move_to_element(driver.find_element_by_xpath('//button[@id="mousehover"]')).perform()
#
# action.move_to_element(driver.find_element_by_id("Top")).click()



"""........................................................................Right click and double click.."""

"""....................................................................working..Right click"""
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get('https://www.google.com/')
# button = driver.find_element_by_xpath("//a[text()='Gmail']")
# action = ActionChains(driver)
# action.context_click(button).perform()

"""....................................................................working..Double click"""
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get('https://www.google.com/')
# button = driver.find_element_by_link_text('Gmail')
# action = ActionChains(driver)
# action.double_click(button).perform()


""".....................................................................................Switch_to_window.."""

"""....................................................................working.."""
# driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# driver.find_element_by_css_selector('button[id="openwindow"]').click()
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element_by_xpath('//div[@style="position: absolute; inset: 0px; box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px inset;"]').click()
#
# driver.find_element_by_xpath("//a[text()='Practice']").click()

#.......................................

# driver.find_element_by_css_selector("a[text()='Practice']").click()
# driver.find_element_by_link_text("Practice").click()
#................................... click is not getting done on practice on new window through link text




""".........................................................................................Switch_to_tab.."""


"""....................................................................working.."""
# driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# driver.find_element_by_id("opentab").click()
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element_by_xpath('//ul[@class="navigation clearfix"]/li[2]/a').click()
#
# #...or..the other way of doing this
# course = driver.find_elements_by_xpath("//a[text()='Courses']")
# for i in course:
#     i.click()


""".................................................................................switch_to.frame"""

#.....................................................................not working

# driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="courses-iframe"]'))

# driver.find_element_by_xpath('//ul[@class="navigation clearfix"]//a[text()="Job Support"]').click() #..no error
# driver.find_element_by_xpath('//ul//a[@href="consulting"]').click()   #..no error
# driver.find_element_by_xpath('//div[@class="nav-outer clearfix"]//a[text()="Job Support"]').click() #..no error
# driver.find_element_by_xpath('///ul[@class="navigation clearfix"]/li[6]/a').click()      #..error



"""........................................table............................................."""


# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# from selenium.webdriver.support.select import Select
# from time import sleep
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.find_element_by_xpath('//div[@class="tableFixHead"]//tr[9]/td[2]').click()
#..or.. driver.find_element_by_xpath("//td[text()='Cricketer']").click()


""".....................................static drop down................................."""

from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
from selenium.webdriver.support.select import Select
from time import sleep
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element_by_xpath('//select[@id="dropdown-class-example"]').click()
driver.find_element_by_xpath('//option[@value="option2"]').click()


# static_dropdown = Select(driver.find_element_by_xpath('//select[@id="dropdown-class-example"]'))
#
# static_dropdown.select_by_visible_text("Option3")
# sleep(1)
# static_dropdown.select_by_visible_text("Option2")
# sleep(1)
# static_dropdown.select_by_visible_text("Option1")
# sleep(1)
# driver.close()



""".....................................dynamic dropdown......................................."""


# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
# from selenium.webdriver.support.select import Select
# from time import sleep
# driver.get("https://cleartrip.com")
#
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//div[@class="p-relative"]/div[1]/input[1]').send_keys('del')
#
# places = driver.find_elements_by_xpath('//p[@style="max-width: 337px;"]')
# for place in places:
#     if place.text == 'Deline, CA - Deline (YWJ)':
#         place.click()
#         print(place.text)





"""............................................all concepts...................................."""

#..1......................................."""popup alert"""

# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)
# popup = driver.switch_to.alert   #..or.. popup = driver.switch_to_alert()
# popup.accept()
# popup.dismiss()


#.. 2......................................."""upload"""


# driver.find_element_by_xpath("............").send_keys("path of the image/file")


#.. ........................................"""Explicit wait"""

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
#
# WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "xapth")))


#.. ........................................."""mouse hover"""


# from selenium.webdriver.common.action_chains import ActionChains
#
# action = ActionChains(driver)
#
# action.move_to_element(driver.find_element_by_xpath(".............").click().perform()
#
# action.move_to_element(driver.find_element_by_xpath('..........................')).click().perform()


#.. ........................................."""Right click and double click"""

# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)
# action.context_click(driver.find_element_by_xpath("..............."))..perform() #RIGHT CLICK
# action.double_click(driver.find_element_by_xpath("................")).perform() #Double Click


#.. ........................................"""switch_to_window""".."""switch_to_tab"""

# driver.switch_to.window(driver.window_handles[1])


#.. ........................................"""switch_to_frame"""

# driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="courses-iframe"]'))





