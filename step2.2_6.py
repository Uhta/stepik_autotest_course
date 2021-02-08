from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
browser.get ('http://suninjuly.github.io/execute_script.html')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input_ans = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_ans)

    input_ans.send_keys(y)
    
    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

    

    
