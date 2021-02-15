import logging
import time

import pytest

from pages.product_page import ProductHelper
from pages.login_page import LoginHelper
from myconfig import *

logging.getLogger('urllib3').setLevel('ERROR')
logging.getLogger('selenium').setLevel('ERROR')

class Test_Stepik:
    @pytest.mark.parametrize('offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, offer):
        url_fin = f"{url_param}{offer}"
        product_page = ProductHelper(browser, url_fin)
        product_page.go_to_site()
        product_page.find_click_add_btn()
        product_page.solve_quiz_and_get_code()
        product_page.find_assert_name("Coders at Work")
        product_page.find_assert_price("19,99 £")

    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductHelper(browser, url_city_stars)
        product_page.go_to_site()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_page = ProductHelper(browser, url_city_stars)
        product_page.go_to_site()
        product_page.should_be_login_link()
        product_page.go_to_login_page()
        product_page.should_be_login_link()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        step_page = ProductHelper(browser, url)
        step_page.go_to_site()
        step_page.find_click_add_btn()
        step_page.solve_quiz_and_get_code()
        step_page.assert_no_success_message()

    def test_guest_cant_see_success_message(self, browser):
        step_page = ProductHelper(browser, url)
        step_page.go_to_site()
        step_page.assert_no_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        step_page = ProductHelper(browser, url)
        step_page.go_to_site()
        step_page.find_click_add_btn()
        step_page.solve_quiz_and_get_code()
        step_page.assert_msg_disappeared()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        main_page = ProductHelper(browser, url_city_stars)
        main_page.go_to_site()
        main_page.find_click_cart_btn()
        main_page.assert_empty_cart()
        main_page.assert_empty_cart_text()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        log_page = LoginHelper(browser, url_login)
        log_page.go_to_site()
        log_page.register_new_user(email, password)
        log_page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        step_page = ProductHelper(browser, url)
        step_page.go_to_site()
        step_page.assert_no_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductHelper(browser, url)
        product_page.go_to_site()
        product_page.find_click_add_btn()
        product_page.solve_quiz_and_get_code()
        product_page.find_assert_name("Coders at Work")
        product_page.find_assert_price("19,99 £")