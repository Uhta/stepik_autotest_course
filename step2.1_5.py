from selenium import webdriver
import time
import math

#определяем функцию для рассчета
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/math.html'
    browser.get(link)

    #считываем элемент и считаем новое значение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #вписываем ответ в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #отмечаем checkbox
    check1 = browser.find_element_by_css_selector("#robotCheckbox")
    check1.click()
    #отмечаем radiobutton
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    #нажимаем на кнопку
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
