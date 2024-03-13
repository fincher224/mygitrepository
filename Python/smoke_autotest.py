import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from faker import Faker

while True:
    print("Приветствую тебя в нашем интернет - магазине\nВыбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
    product = int(input())
    print(product)

    options = webdriver.ChromeOptions()
    path_download = "C:\\Users\\finch\\PycharmProjects\\resourse\\download"
    prefs = {'download.default_directory': path_download}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    g = Service('C:\\Users\\finch\\PycharmProjects\\pythonSelenium\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    base_url = 'https://www.saucedemo.com/'

    driver_g.get(base_url)
    driver_g.maximize_window()
    driver_g.implicitly_wait(10)
    fak = Faker("en_US")
    first_name = fak.first_name()
    last_name = fak.last_name()
    zip_code = fak.random_int()

    user_name = driver_g.find_element(By.XPATH, "//*[@class='input_error form_input']")
    user_name.send_keys('standard_user')
    print('Input login - успешно')
    user_pass = driver_g.find_element(By.CSS_SELECTOR, "#password")
    user_pass.send_keys('secret_sauce')
    print('Input password - успешно')
    user_name.send_keys(Keys.RETURN)
    print('Enter - успешно\n')

    name_locator = driver_g.find_element(By.XPATH, f'(//div[@class="inventory_item"])[{product}]/div[2]/div/a/div')
    value_name_locator = name_locator.text

    price_locator = driver_g.find_element(By.XPATH, f"(// div[@class ='inventory_item_price'])[{product}]")
    value_price_locator = price_locator.text

    def add_item():
        add_1 = driver_g.find_element(By.XPATH, f"(//button[contains(text(), 'Add to cart')])[{product}]")
        add_1.click()
        print(f'You have chosen: {value_name_locator}\nPrice: {value_price_locator}\n')

    def cart_button():
        enter_cart = driver_g.find_element(By.XPATH, '//a[@class ="shopping_cart_link"]')
        enter_cart.click()

    def checkout():
        check = driver_g.find_element(By.XPATH, '//button[@name="checkout"]')
        check.click()

    def user_data():
        first_name_2 = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
        first_name_2.send_keys(first_name)
        print('Input first_name - успешно')
        last_name_2 = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
        last_name_2.send_keys(last_name)
        print('Input last_name - успешно')
        postal_code = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
        postal_code.send_keys(zip_code)
        print('Input postal_code - успешно\n')

    def continue_button():
        button_continue = driver_g.find_element(By.XPATH, "//input[@id='continue']")
        button_continue.click()
        print('Pressing the "continue" key - успешно\n')

    def name_cart():
        name_cart_locator = driver_g.find_element(By.XPATH, '(//div[@class="cart_item"])/div[2]/a/div')
        value_name_cart_locator = name_cart_locator.text
        print(value_name_cart_locator)
        return value_name_cart_locator

    def price_cart():
        price_cart_locator = driver_g.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
        value_price_cart_locator = price_cart_locator.text
        print(value_price_cart_locator)
        return value_price_cart_locator

    if 1 <= product <= 6:
        add_item()
        cart_button()
        checkout()
        user_data()
        continue_button()
        assert value_name_locator == name_cart()
        assert value_price_locator == price_cart()
        print("\nChecking the ratio of the name and price - успешно\n")