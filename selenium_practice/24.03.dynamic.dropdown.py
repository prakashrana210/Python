from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")

from time import sleep

driver.get("https://www.cleartrip.com/flights?dxid=CjwKCAjwrfCRBhAXEiwAnkmKmaGG05pacAAmg2j5uBRsbZPEojetYlxtusaZqOEhytGutAB95uPooBoCS3sQAvD_BwE&gclid=CjwKCAjwrfCRBhAXEiwAnkmKmaGG05pacAAmg2j5uBRsbZPEojetYlxtusaZqOEhytGutAB95uPooBoCS3sQAvD_BwE")

x = driver.find_element_by_xpath("//input[@class='field bw-1 bs-solid w-100p p-2 box-border br-4 fs-2 c-neutral-900 h-8 bc-neutral-100 c-neutral-900 focus:bc-secondary-500 flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 null']")
x.send_keys("ne")

sleep(4)

places = driver.find_elements_by_xpath('//li[@style="padding-top: 6px; padding-bottom: 6px;"]')

for place in places:
    if place.text == "New Delhi, IN - Indira Gandhi Airport (DEL)":
        place.click()

