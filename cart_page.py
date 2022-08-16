import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.notebooks_page import Notebooks_page


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver
        self.notebook = Notebooks_page

    # Locators

    total_cost_locator = "//*[@id='content']/div/div/div[1]/div[2]/aside/aside/div[4]/div[1]/span/span[1]"
    item_id_locator = "//*[@id='content']/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]"
    order_button_locator = "//*[@id='content']/div/div/div[1]/div[2]/aside/aside/div[4]/form/button/span"

    # Getters

    def get_total_cost(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_cost_locator)))

    def get_item_id(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_id_locator)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button_locator)))

    # Actions

    def click_order_button(self):
        self.get_order_button().click()
        print("Click on order button")

    # Methods

    def checkout_1(self):
        self.get_current_url()
        self.assert_word(self.get_total_cost(), "69 999")
        self.click_order_button()
