import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    close_spoiler_locator = "/html/body/div[2]/div[2]/main/div/div[13]"
    login_icon_locator = "//div[@class='HeaderMenu__button HeaderMenu__button_auth IconAndTextWithCount_mainHeader " \
                         "js--HeaderMenu__button_auth IconAndTextWithCount js--IconAndTextWithCount'] "
    user_name_locator = "//input[@class=' InputBox__input js--InputBox__input  js--SignIn__login__container-input']"
    password_locator = "//input[@class=' InputBox__input js--InputBox__input  js--SignIn__password js--InputPassword InputPassword__container-input']"
    submit_button_locator = "//button[@class='SignIn__button js--SignIn__action_sign-in  Button  jsButton Button_theme_primary Button_size_m Button_full-width']"
    catalog_menu_locator = "//button[@class='js--PopupCatalogMenu__button-open PopupCatalogMenu__button-open  Button  jsButton Button_theme_primary-transparent Button_size_m Button_with-icon']"
    electronic_link_locator = "/html/body/div[2]/div[2]/header/div[3]/div/div/div/div/div/menu/div/div[2]/div[2]/div[1]/div[2]/a/span"

    # Getters

    def get_close_spoiler(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_spoiler_locator)))

    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_icon_locator)))

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.submit_button_locator)))

    def get_catalog_menu(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_menu_locator)))

    def get_notebook_link_1(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.electronic_link_locator)))

    # Actions
    def click_close_spoiler(self):
        self.get_close_spoiler().click()
        print("Close spoiler")

    def click_login_icon(self):
        self.get_login_icon().click()
        print("Click login button")

    def input_username(self, user_name):
        self.get_username().send_keys(user_name)
        print("Input login : " + str(user_name))

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password : " + str(password))

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    def click_catalog_menu(self):
        self.get_catalog_menu().click()
        print("Click catalog menu button")

    def click_notebook_link(self):
        self.get_notebook_link_1().click()
        print("Click notebook link button")

    # Methods

    def login_with_error(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_close_spoiler()
        self.get_current_url()
        self.click_login_icon()
        self.input_username("1234test@mail.ru")
        self.input_password("123456")
        self.click_submit_button()

    def go_to_electronic_page(self):
        self.click_catalog_menu()
        self.click_notebook_link()


