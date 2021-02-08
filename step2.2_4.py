from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text


    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    
    s = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

    
