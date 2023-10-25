import pytest

from pages.main_page import MainPage


@pytest.fixture(scope='module')
def search_page(oz_main_page):
    oz_main_page: MainPage
    oz_main_page.go_to_site()
    oz_search_page: Search = oz_main_page.search("Джоан Роулинг")
    yield oz_search_page
    oz_main_page.go_to_site()


def test_search_results_not_empty(search_page):
    assert search_page.get_search_results_by_author()
    assert search_page.is_check_search_request_not_exists()


def test_relevant_search_by_author(search_page):
    all_sub_titles_searched: list[str] = search_page.get_searched_sub_titles()
    assert any("Джоан Роулинг" == searched for searched in all_sub_titles_searched)


def test_filter_by_price(search_page):
    search_page.enter_from_to_price(35, 70)
    all_filtered_prices: list[float] = search_page.get_search_items_price()
    assert all(35 <= filtered_price <= 70 for filtered_price in all_filtered_prices)
