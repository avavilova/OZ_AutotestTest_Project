from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.search_page import Search
from selenium.webdriver import ActionChains


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

    def is_home_sub_menu_displayed_by_hover(self):
        home_sub_menu = self.find_element((By.XPATH, "//a[@href='/home/' and @class='menu-link-action main-nav__list__item ']"))
        action = ActionChains(self.driver)
        action.move_to_element(home_sub_menu).perform()
        home_sub_menu_opened = self.find_element((By.CSS_SELECTOR, "div.global-ppnavlist__inner"))
        return home_sub_menu_opened.is_displayed()







