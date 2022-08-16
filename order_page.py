import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.notebooks_page import Notebooks_page


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver
        self.notebook = Notebooks_page

    # Locators

    first_name_locator = "//input[@name='firstName']"
    last_name_locator = "//input[@name='lastName']"
    phone_number_locator = "//input[@name='phone']"
    delivery_button_locator = "//button[@class='BinTab Tab Button']"
    street_locator = "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/label/input"
    house_locator = "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div[1]/div/label/input"
    bank_card_button_locator = "//*[@id='app-check-out']/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/label[2]"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_locator)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_locator)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number_locator)))

    def get_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_button_locator)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_locator)))

    def get_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house_locator)))

    def get_bank_card_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card_button_locator)))

    # Actions
    def input_first_name(self):
        self.get_first_name().send_keys("Alex")
        print("Input first name")

    def input_last_name(self):
        self.get_last_name().send_keys("Alekseev")
        print("Input last name")

    def input_phone_number(self):
        self.get_phone_number().send_keys("+71234567890")
        print("Input phone number")

    def click_delivery_button(self):
        self.get_delivery_button().click()
        print("Click on delivery address button")

    def input_street(self):
        self.get_street().send_keys("ул.Ленина ")
        print("Input street ")

    def input_house(self):
        self.get_street().send_keys("3")
        print("Input house number ")

    def click_bank_card_button(self):
        self.get_bank_card_button().click()
        print("Click on bank card paying type")

    # Methods

    def end_1(self):
        self.get_current_url()
        self.input_first_name()
        self.input_last_name()
        self.input_phone_number()
        self.click_delivery_button()
        self.input_street()
        self.input_house()
