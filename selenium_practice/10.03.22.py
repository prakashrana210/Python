

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
sleep(5)
expected_prices = {"$25 Virtual Gift Card":25.00, "14.1-inch Laptop": 1590.00, "Build your own cheap computer": 800.00":3}



for gedget, price in expected_prices.items():
    _xpath = f"a[text()='{gadget}']