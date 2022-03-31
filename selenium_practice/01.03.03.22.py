
#................................................................................basic programme

from selenium.webdriver import Chrome

from time import sleep
from selenium.webdriver import Chrome

from time import sleep

#launches a new chrome browser

driver = Chrome("./chromedriver")
driver.maximize_window()

#navigate to demowebshop
driver.get("https://www.naukri.com/")

current_title = driver.title

url = driver.current_url

print(current_title)
print(url)

driver.minimize_window()
sleep(2)

driver.maximize_window()
sleep(2)

driver.close()   #[it close the main page]

#driver.quit()   #[it closed the main site windiow and also popup window]



