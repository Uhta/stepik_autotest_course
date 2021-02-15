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
class ProductPageLocators:
    LOCATOR_BTN_ADD = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    LOCATOR_NAME_EXP = (By.CSS_SELECTOR, "h1:nth-of-type(1)")
    LOCATOR_PRICE_EXP = (By.CSS_SELECTOR, ".price_color:nth-of-type(1)")
    LOCATOR_NAME_ACT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    LOCATOR_PRICE_ACT = (By.XPATH,'//*[@id="messages"]/div[3]/div/p[1]/strong')
    LOCATOR_SUCCESS_MSG = (By.XPATH, '//*[@id="messages"]/div[1]')
    LOCATOR_BTN_CART = (By.PARTIAL_LINK_TEXT, "Посмотреть корзину")
    LOCATOR_BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    LOCATOR_EMPTY_CART = (By.ID, "content_inner")


class ProductHelper(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            logging.debug(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            logging.error("No second alert presented")

    def find_click_add_btn(self):
        self.browser.find_element(*ProductPageLocators.LOCATOR_BTN_ADD).click()

    def find_assert_name(self, exp_name):
        act = self.wait_for_element_presence(ProductPageLocators.LOCATOR_NAME_ACT).text
        try:
            assert exp_name == act, f"Название товаров не совпадает! Ожидаемое: {exp_name}, на странице: {act}"
        except AssertionError:
            logging.error("Проверка названия продукта завершилась с ошибкой", exc_info=True)
            raise AssertionError

    def find_assert_price(self, exp_price):
        act = self.wait_for_element_presence(ProductPageLocators.LOCATOR_PRICE_ACT).text
        try:
            assert exp_price == act, f"Цена товара и корзины не совпадает! Ожидаемое: {exp_price}, на странице: {act}"
        except AssertionError:
            logging.error("Проверка цены продукта завершилась с ошибкой", exc_info=True)
            raise AssertionError

    def assert_no_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.LOCATOR_SUCCESS_MSG) is True, f"Элемент есть на странице!"

    def assert_msg_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.LOCATOR_SUCCESS_MSG) is True

    def find_click_cart_btn(self):
        self.browser.find_element(*ProductPageLocators.LOCATOR_BTN_CART).click()

    def assert_empty_cart(self):
        assert self.is_not_element_present(ProductPageLocators.LOCATOR_BTN_CART) is True, f"Корзина не пуста!"

    def assert_empty_cart_text(self):
        act = self.browser.find_element(*ProductPageLocators.LOCATOR_EMPTY_CART).text
        assert act == exp_empty_cart_text, f"Текст пустой корзины не совпадает с ожидаемым! Ожидаемый: {exp_empty_cart_text}, на странице: {act}"