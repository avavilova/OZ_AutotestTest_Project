import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(scope='module')
def login_page(oz_main_page):
    oz_main_page: MainPage
    oz_main_page.go_to_site()
    oz_login_page: LoginPage = oz_main_page.go_to_login()
    yield oz_login_page
    oz_main_page.go_to_site()


def test_is_phone_login_group_open_by_default(login_page):
    assert login_page.is_phone_login_group_active()


def test_is_email_group_become_active_by_title_select(login_page):
    login_page.select_email_login_group()
    active_group_title = login_page.get_active_login_group_title()
    assert active_group_title == "Электронная почта"
    assert login_page.is_email_login_group_active()


def test_impossible_to_log_in_with_invalid_email(login_page):
    login_page.enter_email_value('kjhkhkjh')
    login_page.click_enter_button_in_email_group()
    assert login_page.is_incorrect_email_msg_exist()
    login_page.clear_filled_email_field()


def test_impossible_to_log_in_with_invalid_password(login_page):
    login_page.enter_email_value('test@test.com')
    login_page.enter_password('jgfjfj')
    login_page.click_enter_button_in_email_group()
    assert login_page.is_incorrect_password_msg_correct() == "Неверный пароль. Если вы потеряли или забыли пароль — восстановите его"
    assert login_page.is_incorrect_password_msg_exist()


def test_is_phone_group_become_active_by_title_select(login_page):
    login_page.select_phone_login_group()
    active_group_title = login_page.get_active_login_group_title()
    assert active_group_title == "Номер телефона"
    assert login_page.is_phone_login_group_active()


def test_imposibble_to_log_in_without_phone_number(login_page):
    login_page.click_send_sms_button_in_phone_group()
    assert login_page.is_phone_error_msg_correct() == 'Введите номер мобильного телефона белорусских опереторов'
    assert login_page.is_phone_error_msg_exist()
