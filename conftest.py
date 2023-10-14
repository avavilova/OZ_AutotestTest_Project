import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from const import BASE_URL
from main_page import MainPage

@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def oz_main_page(driver):
    main_page = MainPage(driver, BASE_URL)
    return main_page
