from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import SearchPageLocators
from pages import BasePage


class Search(BasePage):

    def get_search_results_by_author(self):
        search_results_locator = (By.CSS_SELECTOR, "a.link.product-card__link")
        return self.find_elements(search_results_locator)

    def get_searched_sub_titles(self) -> list[str]:
        sub_titles = self.find_elements((By.CSS_SELECTOR, "div.product-card__subtitle"))
        sub_titles_list = [sub_title.text for sub_title in sub_titles]
        return [sub_title.split(",")[0] for sub_title in sub_titles_list]

    def is_check_search_request_not_exists(self) -> bool:
        return self.is_not_exists(SearchPageLocators.EMPTY_SEARCH_RESULTS)

    def get_search_items_price(self) -> list[float]:
        prices_displayed = self.find_elements((By.CSS_SELECTOR, "div.product-card__cost>.text-primary"))
        prices_list = [price_displayed.text for price_displayed in prices_displayed]
        return [float(price.replace(",", ".").split("р")[0]) for price in prices_list]

    def enter_from_to_price(self, from_price: float, to_price: float):
        from_price_input = self.find_element((By.CSS_SELECTOR, "input[name = 'r_cost[from]']"))
        from_price_input.send_keys(from_price)
        to_price_input = self.find_element((By.CSS_SELECTOR, "input[name = 'r_cost[to]']"))
        to_price_input.send_keys(to_price)
        to_price_input.send_keys(Keys.ENTER)
        self.click_to(SearchPageLocators.SHOW_FILTER_BY_PRICE_RESULTS_LINK)



