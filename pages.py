from __future__ import annotations

from locators import *

import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from const import TIMEOUTS

class BasePage:
    TITLE = None

    def __init__(self, driver: Chrome, url: str):
        self.driver = driver
        self.url = url

    def go_to_site(self, timeout=TIMEOUTS.GET_URL):
        self.driver.get(self.url)
        condition = EC.title_is(self.TITLE)
        return WebDriverWait(self.driver, timeout).until(condition)

    def find_element(self, locator: tuple[str], timeout=TIMEOUTS.FIND_ELEMENT) -> WebElement:
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def find_elements(self, locator: tuple[str], timeout=TIMEOUTS.FIND_ELEMENT) -> list[WebElement]:
        condition = EC.presence_of_all_elements_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def is_exists(self, locator: tuple[str]):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_exists(self, locator: tuple[str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until_not(condition)

    def click_to(self, locator: tuple[str], timeout=TIMEOUTS.FIND_ELEMENT):
        element = self.find_element(locator, timeout)
        element.click()
        return element









