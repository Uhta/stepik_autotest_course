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
class LoginPageLocators:
    LOCATOR_INPUT_EMAIL = (By.CSS_SELECTOR, 'input[name = "registration-email"]')
    LOCATOR_INPUT_PASSWORD = (By.ID, "id_registration-password1")
    LOCATOR_REPEAT_PASSWORD = (By.ID, "id_registration-password2")
    LOCATOR_BTN_REG = (By.NAME, "registration_submit")

class LoginHelper(BasePage):
    def input_email(self, email):
        self.browser.find_element(*LoginPageLocators.LOCATOR_INPUT_EMAIL).send_keys(email)

    def input_password(self, password):
        self.browser.find_element(*LoginPageLocators.LOCATOR_INPUT_PASSWORD).send_keys(password)

    def input_repeat_password(self, password):
        self.browser.find_element(*LoginPageLocators.LOCATOR_REPEAT_PASSWORD).send_keys(password)

    def click_reg_btn(self):
        self.browser.find_element(*LoginPageLocators.LOCATOR_BTN_REG).click()

    def register_new_user(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.input_repeat_password(password)
        self.click_reg_btn()