import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Picked_notebook_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver

    # Locators
    add_to_cart_locator = "//*[@id='product-item-1774287']/div[2]/div/div[5]/div[1]/div[1]/button[1]"
    go_to_cart_locator = "/html/body/div[4]/div[2]/div[1]/div[2]/div/section/header[1]/div/div[2]/button/span"
    notebook_id_locator = "//*[@id='product-item-1774287']/div[2]/div/div[2]/div[1]"

    # Getters

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_locator)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_locator)))

    def get_notebook_id(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.notebook_id_locator)))

    # Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click on add to cart button")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click on cart link button")

    # Methods

    def go_to_cart_page(self):
        self.get_current_url()
        time.sleep(3)
        self.click_add_to_cart_button()
        self.click_go_to_cart()
