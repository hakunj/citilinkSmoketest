import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Notebooks_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver

    # Locators
    cost_slider_locator_1 = "//*[@id='app-filter']/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div[4]"
    search_bar_locator = "//*[@id='app-filter']/div/div[2]/div[2]/div[1]/div[3]/div[1]/input"
    pick_notebook_locator = "/html/body/div[3]/div[2]/main/section/div[1]/div[1]/div[3]/div[1]/section/div[1]/a"
    add_to_cart_locator = "//*[@id='product-item-1774287']/div[2]/div/div[5]/div[1]/div[1]/button[1]"
    go_to_cart_locator = "/html/body/div[4]/div[2]/div[1]/div[2]/div/section/header[1]/div/div[2]/button/span"
    notebook_id_locator = "//*[@id='product-item-1774287']/div[2]/div/div[2]/div[1]"
    # Getters

    def get_cost_slider_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cost_slider_locator_1)))

    def get_search_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_bar_locator)))

    def get_pick_notebook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_notebook_locator)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_locator)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_locator)))

    def get_notebook_id(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.notebook_id_locator)))

    # Actions

    def drag_cost_slider_1(self):
        a = self.get_cost_slider_1()
        self.action.click_and_hold(a).move_by_offset(40, 0).release().perform()
        print("Drag cost slider 1")

    def input_search_bar(self, brand):
        self.get_search_bar().send_keys(brand)
        print("Input brand in search bar : " + brand)

    def click_pick_notebook(self):
        self.get_pick_notebook().click()
        print("Click on notebook")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click on add to cart button")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click on cart link button")


    # Methods

    def select_some_notebook(self):
        self.get_current_url()
        time.sleep(3)
        self.drag_cost_slider_1()
        self.input_search_bar("huawei")
        time.sleep(3)
        self.click_pick_notebook()

