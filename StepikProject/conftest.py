import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

logging.getLogger('urllib3').setLevel('ERROR')
logging.getLogger('selenium').setLevel('ERROR')


def pytest_addoption(parser):  # Получение значения браузера из командной строки для запуска теста
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or IE")


# Объявление браузера. Выполняется для каждого теста
@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = webdriver.Chrome(ChromeDriverManager().install())  # Строка, подключающая веб-драйвер Google Chrome
    elif browser_name == "IE":
        browser = webdriver.Ie("IEDriverServer.exe")  # Строка, подключающая Internet Explorer
    else:
        raise pytest.UsageError("--browser_name should be chrome or IE")
    browser.maximize_window()  # Максимизировать окно браузера
    browser.implicitly_wait(10)  # Установить неявное ожидание 30с
    yield browser
    browser.quit()  # Выйти из браузера по окончанию теста


# Конфигурационные настройки pytest
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata = None  # Очистить данные окружения

    if not os.path.exists('reports'):  # Если нет папки "reports"
        os.makedirs('reports')  # Создать папку "reports"

    config.option.htmlpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"  # Формирование пути к файлу html-report

    if not os.path.exists('logs'):  # Если нет папки logs
        os.makedirs('logs')  # Создать папку logs
    if not config.option.log_file:  # Если в конфигурационном файле pytest.ini не указан параметр log_file
        timestamp = datetime.strftime(datetime.now(), "%d-%m-%Y_%H-%M-%S")  # Определение формата даты и времени
        config.option.log_file = 'logs/' + timestamp + '.log'  # Формирование путь к log-файлу

