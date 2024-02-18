import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from re import sub
from decimal import Decimal

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\finch\\PycharmProjects\\pythonSelenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'

driver_g.get(base_url)
driver_g.maximize_window()

login_standard_user = 'standard_user'
password = 'secret_sauce'


"""Login to the site"""
user_name = driver_g.find_element(By.XPATH, "//*[@class='input_error form_input']")
user_name.send_keys(login_standard_user)
print('Input login - успешно')

user_pass = driver_g.find_element(By.CSS_SELECTOR, "#password")
user_pass.send_keys(password)
print('Input password - успешно')

user_name.send_keys(Keys.RETURN)
print('Enter - успешно\n')


"""Adding products and getting information about them"""

"""Product 1"""
time.sleep(1)
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

prise_product_1 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_prise_product_1 = prise_product_1.text
print('Prise: ' + value_prise_product_1)

add_product_1 = driver_g.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
add_product_1.click()
print('Add product 1 - успешно\n')

"""Product 2"""
product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_2_title_link']")
value_product_2 = product_2.text
print(value_product_2)

prise_product_2 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
value_prise_product_2 = prise_product_2.text
print('Prise: ' + value_prise_product_2)

add_product_2 = driver_g.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")
add_product_2.click()
print('Add product 2 - успешно\n')


"""Go to the cart"""
time.sleep(1)
enter_cart = driver_g.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
enter_cart.click()
print('Go to the cart - успешно\n')


# """Сomparison"""
#
# """Product 1"""
# cart_product_1 = driver_g.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
# value_cart_product_1 = cart_product_1.text
# assert value_product_1 == value_cart_product_1
# print('Сomparison(1) prod 1 - сравнение успешно')
#
# cart_prise_1 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
# value_cart_prise_1 = cart_prise_1.text
# assert value_prise_product_1 == value_cart_prise_1
# print('Сomparison(1) prise 1 - сравнение успешно')
#
# """Product 1"""
# cart_product_2 = driver_g.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
# value_cart_product_2 = cart_product_2.text
# assert value_product_2 == value_cart_product_2
# print('Сomparison(1) prod 2 - сравнение успешно')
#
# cart_prise_2 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
# value_cart_prise_2 = cart_prise_2.text
# assert value_prise_product_2 == value_cart_prise_2
# print('Сomparison(1) prise 2 - сравнение успешно\n')

"""Checkout"""
time.sleep(1)
checkout = driver_g.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button ']")
checkout.click()
print('Checkout - успешно\n')


"""Entering user data"""
time.sleep(1)
first_name = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Mishail')
print('Input first_name - успешно')

last_name = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Dikiy')
print('Input last_name - успешно')

postal_code = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('457586783')
print('Input postal_code - успешно\n')


"""Pressing the "continue" key"""
time.sleep(1)
button_continue = driver_g.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Pressing the "continue" key - успешно\n')


"""Сomparison 2"""

"""Product 1"""
finish_product_1 = driver_g.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_finish_product_1 = finish_product_1.text
assert value_product_1 == value_finish_product_1
print('Сomparison(2) prod 1 - сравнение успешно')

finish_prise_1 = driver_g.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_finish_prise_1 = finish_prise_1.text
assert value_prise_product_1 == value_finish_prise_1
print('Сomparison(2) prise 1 - сравнение успешно')
notadollar_prise_1 = Decimal(sub(r'[^\d.]', '', value_finish_prise_1))

"""Product 2"""
finish_product_2 = driver_g.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
value_finish_product_2 = finish_product_2.text
assert value_product_2 == value_finish_product_2
print('Сomparison(2) prod 2 - сравнение успешно')

finish_prise_2 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_prise_2 = finish_prise_2.text
assert value_prise_product_2 == value_finish_prise_2
print('Сomparison(2) prise 2 - сравнение успешно\n')
notadollar_prise_2 = Decimal(sub(r'[^\d.]', '', value_finish_prise_2))

result = notadollar_prise_1 + notadollar_prise_2


"""Total price"""
summary_prise = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_prise_1 = summary_prise.text
print('Item prise: ' + value_finish_prise_1)
print('Item prise: ' + value_finish_prise_2)
print(value_summary_prise_1)
notadollar_total_prise = Decimal(sub(r'[^\d.]', '', value_summary_prise_1))
assert notadollar_total_prise == result
print('\nСomparison total price - успешно')

