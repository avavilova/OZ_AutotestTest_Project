from __future__ import annotations

from selenium.webdriver.common.keys import Keys
from pages import BasePage
from search_page import Search
from login_page import LoginPage
from locators import MainPageLocators


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





