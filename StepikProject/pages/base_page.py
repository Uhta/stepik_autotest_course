from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_site(self):
        return self.browser.get(self.url)

    def maximize(self):
        self.browser.maximize_window()

    def wait_for_element_presence(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(expected_conditions.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def wait_for_element_visibility(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(expected_conditions.visibility_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def wait_for_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(expected_conditions.element_to_be_clickable(locator),
                                                       message=f'Element is not clickable. Locator:{locator}')

    def wait_for_element_to_be_not_clickable(self, locator, time=10):
        return WebDriverWait(self.browser, time).until_not(expected_conditions.element_to_be_clickable(locator),
                                                           message=f'Element is clickable. Locator:{locator}')

    def is_not_element_present(self, locator):
        try:
            self.wait_for_element_presence(locator)
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.wait_for_element_presence(BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.wait_for_element_presence(BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
