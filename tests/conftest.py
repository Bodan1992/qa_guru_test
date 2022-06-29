# общий файл для текстур на весь проект или модуль распространяются
import pytest
from selene.support.shared import browser
from selenium import webdriver
import os
# browser.config.driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    # browser.driver.set_window_size(2560, 1440)