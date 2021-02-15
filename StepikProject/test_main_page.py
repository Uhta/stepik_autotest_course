import logging
import time

import pytest

from pages.main_page import MainHelper
from myconfig import *

logging.getLogger('urllib3').setLevel('ERROR')
logging.getLogger('selenium').setLevel('ERROR')

class Test_Stepik:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainHelper(browser, url_main)
        main_page.go_to_site()
        main_page.find_click_cart_btn()
        main_page.assert_empty_cart()
        main_page.assert_empty_cart_text()