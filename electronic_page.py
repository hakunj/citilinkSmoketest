import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Electronic_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    notebook_link_locator = "/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/a"

    # Getters

    def get_notebook_button(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.notebook_link_locator)))

    # Actions

    def click_notebook_button(self):
        self.get_notebook_button().click()
        print("Click notebooks link button")

    # Methods

    def link_to_notebooks(self):
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/catalog/noutbuki-i-kompyutery/")
        self.click_notebook_button()
