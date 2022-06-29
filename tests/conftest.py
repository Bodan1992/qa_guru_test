import pytest
from selene.support.shared import browser
from selenium import webdriver
import os



@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')