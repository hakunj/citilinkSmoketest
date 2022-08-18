import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.electronic_page import Electronic_page
from pages.error_page import Error_page
from pages.main_page import Main_page
from pages.notebooks_page import Notebooks_page
from pages.order_page import Order_page
from selenium.webdriver.chrome.options import Options

from pages.picked_notebook_page import Picked_notebook_page


def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\bomj\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)


    print("Start test 1")
    """Заходим на главную страницу и проходим ошибочную авторизацию"""
    mp = Main_page(driver)
    mp.login_with_error()

    """Проверяем верно ли отображается ошибка, url и переходим снова на главную страницу"""
    login = Error_page(driver)
    login.authorization_fail()

    """Переходим на страницу электроники"""
    mp.go_to_electronic_page()

    """Проверям верный ли url и переходим на страницу ноутбуков"""
    electronic = Electronic_page(driver)
    electronic.link_to_notebooks()

    """Выбираем ноутбук по параметрам и """
    notebooks = Notebooks_page(driver)
    notebooks.select_some_notebook()

    """Переходим в корзину"""
    pn = Picked_notebook_page(driver)
    notebooks_id = pn.get_notebook_id().text
    pn.go_to_cart_page()


    """Проверяем тот ли ноутбук у нас и переходим на страницу оформления заказа"""
    cart = Cart_page(driver)
    cart_item_id = cart.get_item_id().text
    assert notebooks_id == cart_item_id
    cart.checkout_1()

    """Заполняем данные о покупателе и место доставки"""
    order = Order_page(driver)
    order.end_1()

    print("Smoke test done well!")
    time.sleep(10)



