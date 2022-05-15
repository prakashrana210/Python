
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
from time import sleep


# driver.get("https://google.com")
# driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys('best thing')
# sleep(2)
# driver.find_element_by_xpath(("//span[@class='QCzoEc z1asCe MZy1Rb']"))

# popup = driver.switch_to_alert()
# popup.dismiss()

# driver.get("https://www.flipkart.com/")
# driver.find_element_by_xpath('//body[@class="fk-modal-visible"]').click()


"""...................................................AJIO........................................................"""


# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://www.ajio.com/")
# action = ActionChains(driver)
# hover = driver.find_element_by_xpath('//a[@title="MEN"]')
# action.move_to_element(hover).perform()
# sleep(1)
# driver.find_element_by_xpath('//a[@href="/s/clothing-4461-74582"]').click()
# sleep(1)
#
#
# name = driver.find_elements_by_class_name("nameCls") #.."div[@class="
# print(type(name))
# print(name)
# discount = driver.find_elements_by_class_name("discount") #.."span[@class="
# #
# print()
#
# """ discount """
#
# import re
# res = []
# for i in discount:
#     res.append(re.findall(r'\d+', i.text))
# print(res)
#
# #.. [['66'], ['46'], ['55'], ['66'], ['66'], ['46'], ['38'], ['45'], ['66'], ['37'], ['45'], ['55'], ['44'], ['51'], ['68'], ['38'], ['10'], ['35'], ['60'], ['50'], ['67'], ['51'], ['20'], ['60'], ['48'], ['20'], ['10'], ['68'], ['30'], ['10'], ['67'], ['47'], ['27'], ['66'], ['56'], ['67'], ['30'], ['30'], ['68']]
#
# print()
#
# """product name and discount"""

# d = {}
# for i in name:
#     for j in discount:
#         emp = " "
#         for k in j.text:
#             if k.isdigit():
#                 emp = emp + k
#         d[i.text] = int(emp[1:])
# print(d)

# # output - {'Jogger Pant with Drawstring Waist': 68, 'Mid-Rise Slim Fit Jeans': 68, 'Checked Slim Fit Shirt with Patch Pocket': 68, 'Joggers with Insert Pockets': 68, 'Straight Track Pants with Insert Pockets': 68, 'Slim Fit Jeans with Whiskers': 68, 'Logo Print Crew-Neck T-shirt': 68, '511 Washed Slim Fit Jeans': 68, 'Pack of 3 Crew-Neck T-shirts': 68, 'Mid-Wash Slim Fit Jeans': 68, 'Washed Slim Fit Jeans': 68, 'Checked Shirt with Patch Pocket': 68, 'Trackpants with Ribbed Drawstring Waist': 68, 'Fastdry Active Crew-Neck T-shirt': 68, 'Pack of 3 Briefs with Logo Print Waistband': 68, 'Slim Fit Joggers with Elasticated Drawstring Waist': 68, 'Slim Fit Track Pants with Insert Pockets': 68, 'Striped Cotton Shirt with Patch Pocket': 68, 'Checked Polo T-shirt': 68, 'Flat-Front Jogger Pants': 68, 'Stripes Regular-fit Polo T-shirt': 68, 'Leaf Print Polo T-shirt': 68, 'Fastdry Active Panelled Track Pants': 68, 'Fastdry Active Essential Track Pants': 68, 'Leaf Print Shirt with Patch Pocket': 68, 'Striped Shirt with Patch Pocket': 68, 'Cotton Henley T-shirt': 68, '513 Straight Fit Washed Jeans': 68, 'Solid Polo Neck T-shirt': 68, 'Bermuda Shorts with Insert Pockets': 68, 'Crew-Neck T-shirt with Logo Print': 68}
#
# print()
#
# """  highest discount  """
#
# sequence = sorted(d.items(), key=lambda i: i[-1])
# print("highest discount", "=", sequence[-1][-1])
#
# #.. highest discount = 67
#
# print()
#
#
#
# for i,v in zip(name, discount):
#     print(i.text, v.text)


# <class 'list'>
# [<selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="55810ce7-c8c9-4c00-a1c9-dc7c2f940d41")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="04309873-0888-4e2a-b2cb-94f30812ebd8")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="25905d73-4892-4efa-8124-731ec4799490")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="86d0dd5a-c7ed-4e77-b75c-703629ff7b75")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="b2979b0d-d723-4b9a-a38f-ee64f614d571")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="4ffeeac1-dee4-4d43-9970-bacdf8f5d593")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="08b1d54b-098b-4bb2-8122-168f9088997c")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="628ff7d9-3858-4ab8-a022-e48c68358c65")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="58f82f11-678a-4e9b-9de1-eb415a1b6916")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="0bb5873c-f395-49af-9f94-2af03547c121")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="c7eeaa15-d4fb-4323-b5a7-e30cbd2e82f8")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="b86fa78c-0e1a-41d5-aafd-30e88498eb07")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="47d25617-2d46-46cb-a81d-1b0717067c67")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="651ddf29-3c6d-49f1-b658-7ff9a75d142a")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="429e1598-9d68-4de7-9feb-1c5fb73e41fa")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="c186ba62-2c2e-4a68-b133-09b5ab281640")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="bf9b4844-c379-4833-9708-991f4586d18e")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="a74d3dd6-e563-4bae-b182-96394be93f2e")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="e1327ff7-32ef-4efa-9110-fdf3a5d7532d")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="6efd81f9-5958-481f-a3ef-3ef601f55c87")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="707347e2-cbf3-4de3-a593-f40296523fb8")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="671a0bd3-1ee6-497e-8f0d-9807a01368a7")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="72eb1654-2d5a-4504-98c3-be2ff7ddd1ab")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="4f86a473-a74b-4b95-bcdb-7a56e43d8729")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="3f36263e-f772-462a-bd8b-65ef349fc37b")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="3909b642-363f-4cc4-a541-f1d5e29ada88")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="5d5a2977-fb7c-444a-9778-ea094cfb47f6")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="108650f4-b661-4c35-83b9-06a293dfac41")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="e055727c-082d-4fd6-aa00-b4660e971e60")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="a85a75fc-475d-4691-9aaf-49af9d13d4bc")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="dbcb51d3-9d94-4d73-be06-9be4b8b75013")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="cc1f13e9-4920-42f0-9384-0fdd1238db30")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="7a1f97f3-c959-4fc8-80b7-df6297822eb1")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="449a813a-cadc-4281-af94-574a505ba942")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="92dd80b3-26cb-4fe0-ba84-668df1bbd7e4")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="67f50dc6-dc07-440e-bd36-4932262206de")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="f72bd9d9-401c-4ea7-8152-ee98cc3d088b")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="917ea16a-9d0f-467e-8518-9b6dcc6388b0")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="7f0a04f8-6c81-43e7-a6f1-76ff1c08d139")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="1c1f162c-a0a5-4d11-a022-2d024957b53c")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="3b6e7f0e-582f-48e2-9345-3ae1a0731259")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="53981008-f73f-4c0a-a1c9-7c403a0c7a1c")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="320ab5b5-6588-4afb-ae85-f57f1a6a8535")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="fbfe5f0b-d8ed-4bbb-ad77-f18a88ccefce")>, <selenium.webdriver.remote.webelement.WebElement (session="c81c7944694bbec84c8f9b189fee975a", element="5e885e80-5a09-4b37-8750-b7be435e88bd")>]
#
# [['66'], ['46'], ['55'], ['66'], ['66'], ['46'], ['38'], ['45'], ['66'], ['37'], ['45'], ['55'], ['44'], ['51'], ['68'], ['38'], ['10'], ['35'], ['60'], ['50'], ['67'], ['51'], ['20'], ['60'], ['48'], ['20'], ['10'], ['68'], ['30'], ['10'], ['67'], ['47'], ['27'], ['66'], ['56'], ['67'], ['30'], ['30'], ['68']]
#
# {'Jogger Pant with Drawstring Waist': '(68% off)', 'Mid-Rise Slim Fit Jeans': '(68% off)', 'Checked Slim Fit Shirt with Patch Pocket': '(68% off)', 'Joggers with Insert Pockets': '(68% off)', 'Straight Track Pants with Insert Pockets': '(68% off)', 'Slim Fit Jeans with Whiskers': '(68% off)', 'Logo Print Crew-Neck T-shirt': '(68% off)', '511 Washed Slim Fit Jeans': '(68% off)', 'Pack of 3 Crew-Neck T-shirts': '(68% off)', 'Mid-Wash Slim Fit Jeans': '(68% off)', 'Washed Slim Fit Jeans': '(68% off)', 'Checked Shirt with Patch Pocket': '(68% off)', 'Trackpants with Ribbed Drawstring Waist': '(68% off)', 'Fastdry Active Crew-Neck T-shirt': '(68% off)', 'Pack of 3 Briefs with Logo Print Waistband': '(68% off)', 'Slim Fit Joggers with Elasticated Drawstring Waist': '(68% off)', 'Slim Fit Track Pants with Insert Pockets': '(68% off)', 'Striped Cotton Shirt with Patch Pocket': '(68% off)', 'Checked Polo T-shirt': '(68% off)', 'Flat-Front Jogger Pants': '(68% off)', 'Stripes Regular-fit Polo T-shirt': '(68% off)', 'Leaf Print Polo T-shirt': '(68% off)', 'Fastdry Active Panelled Track Pants': '(68% off)', 'Fastdry Active Essential Track Pants': '(68% off)', 'Leaf Print Shirt with Patch Pocket': '(68% off)', 'Striped Shirt with Patch Pocket': '(68% off)', 'Cotton Henley T-shirt': '(68% off)', '513 Straight Fit Washed Jeans': '(68% off)', 'Solid Polo Neck T-shirt': '(68% off)', 'Bermuda Shorts with Insert Pockets': '(68% off)', 'Crew-Neck T-shirt with Logo Print': '(68% off)'}
#
# Jogger Pant with Drawstring Waist (66% off)
# Mid-Rise Slim Fit Jeans (46% off)
# Checked Slim Fit Shirt with Patch Pocket (55% off)
# Joggers with Insert Pockets (66% off)
# Straight Track Pants with Insert Pockets (66% off)
# Mid-Rise Slim Fit Jeans (46% off)
# Slim Fit Jeans with Whiskers (38% off)
# Slim Fit Jeans with Whiskers (45% off)
# Straight Track Pants with Insert Pockets (66% off)
# Logo Print Crew-Neck T-shirt (37% off)
# 511 Washed Slim Fit Jeans (45% off)
# Pack of 3 Crew-Neck T-shirts (55% off)
# Checked Slim Fit Shirt with Patch Pocket (44% off)
# Mid-Wash Slim Fit Jeans (51% off)
# Washed Slim Fit Jeans (68% off)
# Checked Shirt with Patch Pocket (38% off)
# Mid-Wash Slim Fit Jeans (10% off)
# Trackpants with Ribbed Drawstring Waist (35% off)
# Fastdry Active Crew-Neck T-shirt (60% off)
# Pack of 3 Briefs with Logo Print Waistband (50% off)
# Slim Fit Jeans with Whiskers (67% off)
# Slim Fit Joggers with Elasticated Drawstring Waist (51% off)
# Slim Fit Track Pants with Insert Pockets (20% off)
# Striped Cotton Shirt with Patch Pocket (60% off)
# Mid-Wash Slim Fit Jeans (48% off)
# Checked Polo T-shirt (20% off)
# Flat-Front Jogger Pants (10% off)
# Stripes Regular-fit Polo T-shirt (68% off)
# Leaf Print Polo T-shirt (30% off)
# Fastdry Active Panelled Track Pants (10% off)
# Checked Shirt with Patch Pocket (67% off)
# Fastdry Active Essential Track Pants (47% off)
# Leaf Print Shirt with Patch Pocket (27% off)
# Striped Shirt with Patch Pocket (66% off)
# Cotton Henley T-shirt (56% off)
# 513 Straight Fit Washed Jeans (67% off)
# 511 Washed Slim Fit Jeans (30% off)
# Joggers with Insert Pockets (30% off)
# Solid Polo Neck T-shirt (68% off)


"""................product name which has hightest price......................"""

from selenium.webdriver.common.action_chains import ActionChains
driver.get("https://www.ajio.com/")
women = driver.find_element_by_xpath('//a[@title="WOMEN"]')

action = ActionChains(driver)
action.move_to_element(women).perform()

driver.find_element_by_xpath('//a[@href="/s/clothing-4461-75482"]').click()

#.. driver.find_element_by_xpath("//div[text()='Floral Print Straight Kurta Suit Set']/../..//span[text()='₹900']").click()

products = driver.find_elements_by_class_name('nameCls')
prices = driver.find_elements_by_xpath('//span[@class="price  "]')

import re

# d = {}
# for i in products:
#     for j in prices:
#         d[i.text] = j.text
# print(d)

#.. {'Floral Print Straight Kurta Suit Set': '₹896', 'Indian Lehenga Choli Set with Dupatta': '₹896', 'Solid Fit & Flare Dress': '₹896', 'Printed Anarkali Kurta Suit Set': '₹896', 'Polka-Dot Print A-line Kurta': '₹896', 'Mid-Wash Skinny Jeans': '₹896', 'Embroidered Round-Neck Straight Kurta Set': '₹896', 'Printed Kurta Suit Set': '₹896', 'Floral Print Flared Kurta': '₹896', 'Tie & Dye Crew-Neck T-shirt': '₹896', 'Solid Straight Kurta Set': '₹896', 'Embroidered Straight Kurta Set with Dupatta': '₹896', 'Typographic Print Crew-Neck T-shirt': '₹896', 'Floral Embroidered Straight Kurta': '₹896', 'Floral Print Kurta Set with Dupatta': '₹896', '710 Light-Wash Super Skinny Jeans': '₹896', 'Wide-Leg Jeans': '₹896', 'Flat-Front Wide Fit Trousers': '₹896', 'Gown Dress with Bow': '₹896', 'Embellished Georgette Skirt- Suit-Set': '₹896', 'Bandhani Print Anarkali Kurta Set': '₹896', 'Embroidered Flared Kurta': '₹896', 'Embellished Straight Kurta Set': '₹896', 'High-Rise Trousers': '₹896', 'Bandhej Straight Kurta Set': '₹896', 'Mid-Rise Track Pants with Elasticated Waist': '₹896', 'Floral Print Crew-Neck T-shirt': '₹896', 'Indian Straight Kurta Set with Dupatta': '₹896', 'Lightly Washed & Distressed Slim Fit Jeans': '₹896', 'V-neck Peplum Top with Bow Applique': '₹896', 'Floral Embroidered Anarkali Kurta': '₹896', 'Swiss-Dot Peplum Top': '₹896', 'Printed Round-Neck Straight Kurta': '₹896', 'Lightly Washed Relaxed Jeans': '₹896', 'Embellished 3/4t-Sleeve Flared Kurta': '₹896', 'Solid Shirt with Trousers Set': '₹896', 'Floral Embroidered Kurta Sets': '₹896', 'Printed Flared Kurta with Collar-Neck': '₹896', 'Floral Print Slim Fit Crew-Neck T-shirt': '₹896', 'Graphic Straight Kurta Set': '₹896'}


# D = {}
# res = []
# for i in products:
#     for j in prices:
#         res.append(j.text)
#         D[i.text] = j.text[1:]
# print(D)


# res = sorted(D.items(), key = lambda i: i[-1])
# print(res)
# print(res[-1])
# print("highest_price :", int(res[-1][-1]))

# {'Solid Fit & Flare Dress': '4,199', 'Printed Anarkali Kurta Suit Set': '4,199', 'Polka-Dot Print A-line Kurta': '4,199', 'Embroidered Round-Neck Straight Kurta Set': '4,199', 'Printed Kurta Suit Set': '4,199', 'Floral Print Flared Kurta': '4,199', 'Tie & Dye Crew-Neck T-shirt': '4,199', 'Solid Straight Kurta Set': '4,199', 'Embroidered Straight Kurta Set with Dupatta': '4,199', 'Typographic Print Crew-Neck T-shirt': '4,199', 'Floral Embroidered Straight Kurta': '4,199', '710 Light-Wash Super Skinny Jeans': '4,199', 'Wide-Leg Jeans': '4,199', 'Flat-Front Wide Fit Trousers': '4,199', 'Gown Dress with Bow': '4,199', 'Embellished Georgette Skirt- Suit-Set': '4,199', 'Bandhani Print Anarkali Kurta Set': '4,199', 'Embellished Straight Kurta Set with Dupatta': '4,199', 'Embroidered Flared Kurta': '4,199', 'Embellished Straight Kurta Set': '4,199', 'High-Rise Trousers': '4,199', 'Bandhej Straight Kurta Set': '4,199', 'Mid-Rise Track Pants with Elasticated Waist': '4,199', 'Floral Print Crew-Neck T-shirt': '4,199', 'Lightly Washed & Distressed Slim Fit Jeans': '4,199', 'V-neck Peplum Top with Bow Applique': '4,199', 'Floral Embroidered Anarkali Kurta': '4,199', 'Swiss-Dot Peplum Top': '4,199', 'Printed Round-Neck Straight Kurta': '4,199', 'Embellished 3/4t-Sleeve Flared Kurta': '4,199', 'Solid Shirt with Trousers Set': '4,199', 'Floral Embroidered Kurta Sets': '4,199', 'Printed Flared Kurta with Collar-Neck': '4,199', 'Floral Print Slim Fit Crew-Neck T-shirt': '4,199', 'Graphic Straight Kurta Set': '4,199', 'Indian Straight Kurti': '4,199', 'Mid-Rise Jeans with 5-Pockets': '4,199', 'Striped Round-Neck T-shirt': '4,199', 'Pants with Drawstring Waist': '4,199', 'Floral Print Woven Top & Pyjamas Set': '4,199', 'Block Print Straight Kurta Set': '4,199', 'Floral Print Lehenga Choli Set with Dupatta': '4,199'}
# ('Floral Print Lehenga Choli Set with Dupatta', '4,199')
# highest_price : 4,199


# #..{'Floral Print Straight Kurta Suit Set': '896', 'Indian Lehenga Choli Set with Dupatta': '896', 'Solid Fit & Flare Dress': '896', 'Printed Anarkali Kurta Suit Set': '896', 'Polka-Dot Print A-line Kurta': '896', 'Mid-Wash Skinny Jeans': '896', 'Embroidered Round-Neck Straight Kurta Set': '896', 'Printed Kurta Suit Set': '896', 'Floral Print Flared Kurta': '896', 'Tie & Dye Crew-Neck T-shirt': '896', 'Solid Straight Kurta Set': '896', 'Embroidered Straight Kurta Set with Dupatta': '896', 'Typographic Print Crew-Neck T-shirt': '896', 'Floral Embroidered Straight Kurta': '896', 'Floral Print Kurta Set with Dupatta': '896', '710 Light-Wash Super Skinny Jeans': '896', 'Wide-Leg Jeans': '896', 'Flat-Front Wide Fit Trousers': '896', 'Gown Dress with Bow': '896', 'Embellished Georgette Skirt- Suit-Set': '896', 'Bandhani Print Anarkali Kurta Set': '896', 'Embroidered Flared Kurta': '896', 'Embellished Straight Kurta Set': '896', 'High-Rise Trousers': '896', 'Bandhej Straight Kurta Set': '896', 'Mid-Rise Track Pants with Elasticated Waist': '896', 'Floral Print Crew-Neck T-shirt': '896', 'Indian Straight Kurta Set with Dupatta': '896', 'Lightly Washed & Distressed Slim Fit Jeans': '896', 'V-neck Peplum Top with Bow Applique': '896', 'Floral Embroidered Anarkali Kurta': '896', 'Swiss-Dot Peplum Top': '896', 'Printed Round-Neck Straight Kurta': '896', 'Lightly Washed Relaxed Jeans': '896', 'Embellished 3/4t-Sleeve Flared Kurta': '896', 'Solid Shirt with Trousers Set': '896', 'Floral Embroidered Kurta Sets': '896', 'Printed Flared Kurta with Collar-Neck': '896', 'Floral Print Slim Fit Crew-Neck T-shirt': '896', 'Graphic Straight Kurta Set': '896'}
















