
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
from time import sleep

driver.get("file:///C:/Users/Admin/Downloads/demo.html")

# checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')



# for item in checkboxes[::-1]:
#     item.click()
#     sleep(1)

# for item in checkboxes[::-1]:
#     item.click()
#     break


# for item in checkboxes[:1]:
#     item.click()


# for item in checkboxes[::-1]:
#     item.click()

# for item in checkboxes[::2]:
#     item.click()

# for item in checkboxes[::-2]:
#     item.click()
#     sleep(0.2)

#.............................................................not working
# from selenium.webdriver.support.select import Select
# for item in checkboxes[::-1]:
#     item.click()
#     sleep(1)
# Select.deselect_all(checkboxes)

#.............................................................not working
# from selenium.webdriver.support.select import Select
# lst_box = driver.find_elements_by_xpath('//input[@type="checkbox"]')
# select = Select(lst_box)
# select.select_by_index(1)



""".................input with zip....working..............."""

# input_ = driver.find_elements_by_xpath('//input[@type="text"]')
# text = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "shiv", "Rana"]
#
# for i,v in zip(input_, text):
#     i.send_keys(v)
#     sleep(1)


"""............................upload..................................."""

# driver.find_element_by_xpath('//input[@type="file"]').send_keys('C:\\Users\\Admin\\Desktop\\demo.pic')


"""............................visibility of element located......................."""


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
#
# driver.get("file:///C:/Users/Admin/Downloads/loading.html")
#
#
# class _visibility_of_element_located(visibility_of_element_located):         # inherit visibility_of_element_located class in child class _visibility_of_element_located
#     def _call_(self, driver):
#         result = super()._call(driver)                    # calling parent class(object class) __call_ method and pass driver as an argument:
#         if isinstance(result, WebElement):
#             print("checking for enable")
#             return result.is_enabled()
#         return result
#
#
# wait = WebDriverWait(driver, 11)
# v = _visibility_of_element_located(("name", "fname"))
# wait.until(v)
# driver.find_element_by_name("fname").send_keys("Hello")


"""......................................locators......................................."""

# driver.get("https://www.google.com/")
# driver.find_element_by_xpath('//a[@class="gb_d"]').click()
# driver.find_element_by_class_name("gb_d").click()
# driver.find_element_by_link_text("Gmail").click()
# driver.find_element_by_partial_link_text("ma").click()            #can also take middle part
# driver.find_element_by_css_selector('a[class="gb_d"]').click()

# driver.find_element_by_css_selector('a[text()="Gmail"]').click()  #..selenium.common.exceptions.InvalidSelectorException: Message: invalid selector: An invalid or illegal selector was specified









