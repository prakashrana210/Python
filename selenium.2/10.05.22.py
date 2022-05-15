

"""........................................popup alert......................................"""

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from time import sleep
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element_by_id("alertbtn").click()
# sleep(2)
# popup = driver.switch_to.alert
# popup.accept()
# sleep(2)
# driver.quit()

"""....................................upload......................................."""

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from time import sleep
# driver.get("https://the-internet.herokuapp.com/upload")
# sleep(2)
# driver.find_element_by_id("file-upload").send_keys("C:\\Users\\Admin\\Desktop\\hello.JPG")
# sleep(2)
# driver.find_element_by_id("file-submit").click()
# sleep(2)
# driver.quit()


"""....................................EXPLICIT WAIT....................................."""


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
# for i in checkboxes:
#     i.click()
# WebDriverWait(driver, 30).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "........")))
# # WebDriverWait(driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "......")))

# driver.quit()


"""......................................mouse hover........................................."""

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://www.myntra.com/")
#
# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath('//a[@data-index="1"]')).perform()
# sleep(2)
# action.move_to_element(driver.find_element_by_xpath('//a[@data-reactid="31"]')).click().perform()
# sleep(2)
# driver.close()

"""......................................Right click and double clic........................"""
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from time import sleep
#
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get('https://www.google.com/')
# action = ActionChains(driver)
# action.context_click(driver.find_element_by_link_text("Images")).perform()
# sleep(2)
# driver.close()

#......since previous page is closed (due to command-driver.close()), now need to give the below 2 commands again, not taking previous commands

# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from selenium.webdriver.common.action_chains import ActionChains

# driver.get('https://www.google.com/')
# action = ActionChains(driver)
# action.double_click(driver.find_element_by_link_text("Gmail")).perform()
#
# driver.close()


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from time import sleep
#
# driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="courses-iframe"]'))
#
# driver.find_element_by_xpath('//ul[@class="navigation clearfix"]//a[text()="Job Support"]').click() #..no error
# # driver.find_element_by_xpath('//ul//a[@href="consulting"]').click()   #..no error
# # driver.find_element_by_xpath('//div[@class="nav-outer clearfix"]//a[text()="Job Support"]').click() #..no error
# # driver.find_element_by_xpath('///ul[@class="navigation clearfix"]/li[6]/a').click()      #..error


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")
# from time import sleep
# driver.get("https://google.com")
# sleep(2)
# driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys("prakash rana")
# driver.find_element_by_xpath('//input[@value="Google Search"]').click()
# # driver.find_element_by_xpath('//div[@class="CqAVzb lJ9FBc"]//input[@class="gNO89b"]').click()




from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\selenium_practice\\chromedriver.exe")

driver.implicitly_wait(2)
from time import sleep
driver.get("https://google.com")
driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys("prakash rana")
# sleep(2)
driver.find_element_by_xpath('//input[@value="Google Search"]').click()








