from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import MainPageLocators
from login_page import LoginPage
from pages import BasePage
from search_page import Search


class MainPage(BasePage):
    TITLE = 'OZ.by — интернет-магазин. Книги, игры, косметика, товары для дома, творчества, подарки, продукты. Доставка по Беларуси.'

    def search(self, request_string: str):
        search_input = self.click_to(MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(request_string)
        search_input.send_keys(Keys.ENTER)
        return Search(self.driver, self.driver.current_url)

    def go_to_login(self):
        self.click_to(MainPageLocators.LOGIN_BUTTON)
        return LoginPage(self.driver, self.driver.current_url)

    def unpin_books_catalog(self):
        self.click_to((By.XPATH, "//a[@title='Открепить' and @href='/#staticmenu_header_books']"))

    def is_static_books_menu_pinned(self):
        return self.is_exists(MainPageLocators.BOOKS_CONTAINER_GRID_PIN)

    def is_static_books_menu_unpinned(self):
        return self.is_exists(MainPageLocators.BOOKS_CONTAINER_GRID_NOPIN)

    def scroll_to_books_catalog(self):
        self.scroll_to_element((By.XPATH, "//h2//a[text()='Книги']"))







