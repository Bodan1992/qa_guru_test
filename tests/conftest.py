import pytest
from selene.support.shared import browser
from selenium import webdriver
import os



@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    #browser.driver.set_window_size(2560, 1440) - для указания размера окна
    # browser.config.wait_for_no_overlap_found_by_js = True - убрать перекрытие в футере