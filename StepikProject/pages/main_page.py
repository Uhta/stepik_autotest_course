import logging
import math
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from myconfig import *
logging.getLogger('urllib3').setLevel('ERROR')
logging.getLogger('selenium').setLevel('ERROR')

# Локаторы
class MainPageLocators:
    LOCATOR_BTN_CART = (By.PARTIAL_LINK_TEXT, "Посмотреть корзину")
    LOCATOR_BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    LOCATOR_EMPTY_CART = (By.ID, "content_inner")

class MainHelper(BasePage):
    def find_click_cart_btn(self):
        self.browser.find_element(*MainPageLocators.LOCATOR_BTN_CART).click()

    def assert_empty_cart(self):
        assert self.is_not_element_present(MainPageLocators.LOCATOR_BTN_CART) is True, f"Корзина не пуста!"

    def assert_empty_cart_text(self):
        act = self.browser.find_element(*MainPageLocators.LOCATOR_EMPTY_CART).text
        assert act == exp_empty_cart_text, f"Текст пустой корзины не совпадает с ожидаемым! Ожидаемый: {exp_empty_cart_text}, на странице: {act}"