from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input_ans = browser.find_element_by_id("answer")
    input_ans.send_keys(y)
    

    button_sub = browser.find_element_by_css_selector("button[type='submit']")
    button_sub.click()

finally:
    time.sleep(10)
    browser.quit()
