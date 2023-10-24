import time

import pytest

from pages.main_page import MainPage


@pytest.fixture(scope='module')
def main_page(oz_main_page):
    oz_main_page: MainPage
    oz_main_page.go_to_site()
    yield oz_main_page
    oz_main_page.go_to_site()

def test_home_menu_is_displayed_by_hover(main_page):
    assert main_page.is_home_sub_menu_displayed_by_hover()

@pytest.mark.xfail(reason = "Couldn't scroll to pin element")
def test_hide_static_books_menu(main_page):
    main_page: MainPage
    main_page.scroll_page_down()
    time.sleep(2)
    main_page.scroll_to_books_catalog()
    assert main_page.is_static_books_menu_pinned()
    time.sleep(5)
    main_page.unpin_books_catalog()
    time.sleep(2)
    assert main_page.is_static_books_menu_unpinned()
