from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Petr")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("petrivanov@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
