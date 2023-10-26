from __future__ import annotations

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from const import TIMEOUTS


class BasePage:
    TITLE = None

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url

    def go_to_site(self, timeout=TIMEOUTS.GET_URL):
        self.driver.get(self.url)
        condition = EC.title_is(self.TITLE)
        return WebDriverWait(self.driver, timeout).until(condition)

    def find_element(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT) -> WebElement:
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    # def find_clickable_element(self, locator: tuple[str], timeout=TIMEOUTS.FIND_ELEMENT) -> WebElement:
    #     condition = EC.element_to_be_clickable(locator) if clickable else EC.presence_of_element_located(locator)
    #     return WebDriverWait(self.driver, timeout).until(condition)

    def find_elements(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT) -> list[WebElement]:
        condition = EC.presence_of_all_elements_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def is_exists(self, locator: tuple[any, str]) -> bool:
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_exists(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until_not(condition)

    def click_to(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT):
        element = self.find_element(locator, timeout)
        element.click()
        return element

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def scroll_to_element(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT):
        js_code = "arguments[0].scrollIntoView();"
        element = self.find_element(locator, timeout)
        self.driver.execute_script(js_code, element)
