import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Error_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    enter_button_locator = "//button[@id='passp:sign-in']"
    error_locator = "//div[@class='LoginPageLayout__error-message']"
    main_page_button = "/html/body/div[2]/div[2]/header/div[1]/div[1]/div/div/a/svg"

    #Getters


    def get_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.error_locator)))


    #Actions



    #Methods

    def authorization_fail(self):

        self.get_current_url()
        self.assert_url("https://www.citilink.ru/login/?_from=https%3A%2F%2Fwww.citilink.ru%2F&error=10")
        self.assert_word(self.get_error(), "Неверный логин или пароль")
        self.driver.back()
