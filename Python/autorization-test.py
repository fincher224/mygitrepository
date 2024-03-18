import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from login_page import Login_page

class Dz():
    def test_dz(self):
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
        login = Login_page(driver_g)
        driver_g.implicitly_wait(10)

        def comparison(self):
            product = driver_g.find_element(By.XPATH, '//span[@class="title"]')
            value_product = product.text
            assert value_product == 'Products'
            print("Comparison - successes")

        def logout(self):
            gamburg = driver_g.find_element(By.XPATH, '//button[@id ="react-burger-menu-btn"]')
            gamburg.click()
            time.sleep(1)
            logout_button = driver_g.find_element(By.XPATH, '//a[@id ="logout_sidebar_link"]')
            logout_button.click()
            print('Logout - successes\n')

        def check():
            check_1 = driver_g.find_element(By.XPATH, '//div[@class="error-message-container error"]')
            value_check_1 = check_1.text
            print(value_check_1)
            return value_check_1

        login_name_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user','error_user', 'visual_user']
        login_password = 'secret_sauce'

        for f in login_name_list:
            try:
                print('USER NAME: ' + f)
                login.autorization(f, login_password)
                comparison(self)
                logout(self)
            except:
                check()
                driver_g.refresh()

test = Dz()
test.test_dz()