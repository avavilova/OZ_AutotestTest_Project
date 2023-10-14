from __future__ import annotations

from selenium.webdriver.common.by import By
from pages import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def select_email_login_group(self):
        self.click_to(LoginPageLocators.EMAIL_LOGIN_GROUP_LINK)

    def select_phone_login_group(self):
        self.click_to(LoginPageLocators.PHONE_LOGIN_GROUP_LINK)

    def is_email_login_group_active(self):
        return self.is_exists((By.XPATH, "//div[@data-tab-content = 'email' and @class = 'i-popup__tab-item i-popup__tab-item_active']"))

    def is_phone_login_group_active(self):
        return self.is_exists((By.XPATH, "//div[@data-tab-content = 'phone' and @class = 'i-popup__tab-item i-popup__tab-item_active']"))

    def get_active_login_group_title(self):
        active_login_group_title = self.find_element((By.CSS_SELECTOR, 'a.i-nav-tabs__link.i-nav-tabs__link_active'))
        return active_login_group_title.text

    def enter_email_value(self, email_value: str):
        email_input = self.click_to(LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email_value)

    def clear_filled_email_field(self):
        self.click_to((By.XPATH, "//div[@class = 'i-input-group__cell']//input[@type = 'email']")).clear()


    def enter_password(self, password_value: str):
        password_input = self.click_to(LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password_value)

    def click_enter_button_in_email_group(self):
        self.click_to(LoginPageLocators.ENTER_BUTTON)

    def is_incorrect_email_msg_exist(self):
        return self.is_exists((By.XPATH, "//div[@id = 'test']//div[text()='Введите корректный адрес электронной почты']"))

    def is_incorrect_password_msg_exist(self):
        return self.is_exists((By.XPATH, "//div[text()='Неверный пароль. Если вы потеряли или забыли пароль — ']"))

    def is_incorrect_password_msg_correct(self):
        password_error_msg = self.find_element((By.XPATH, "//div[text()='Неверный пароль. Если вы потеряли или забыли пароль — ']"))
        return password_error_msg.text

    def click_send_sms_button_in_phone_group(self):
        self.click_to(LoginPageLocators.SEND_SMS_BUTTON)

    def is_phone_error_msg_exist(self):
        return self.is_exists((By.XPATH, "//div[text()='Введите номер мобильного телефона белорусских опереторов']"))

    def is_phone_error_msg_correct(self):
        phone_error_msg = self.find_element((By.XPATH, "//div[text()='Введите номер мобильного телефона белорусских опереторов']"))
        return phone_error_msg.text





    # def get_subjects(self) -> tuple[str]:
    #     return tuple([option.text for option in self.get_subject_options()])
    #
    # def set_subject(self, subject: str):
    #     self.click_to((By.XPATH, '//select[@name="themeId"]'))
    #     self.click_to((By.XPATH, f'//select[@name="themeId"]/option[contains(text(), "{subject}")]'))
    #
    # def get_current_subject_text(self) -> str:
    #     for option in self.get_subject_options():
    #         if option.is_selected:
    #             return option.text
    #     else:
    #         raise Exception('No options selected in subject dropdown')
    #
    # def click_to_personal_agreement_checkbox(self):
    #     wrapper = self.find_element((By.CSS_SELECTOR, '.base-checkbox__square_personalagreement'))
    #     wrapper.click()
    #     time.sleep(2)
    #
    # def is_personal_agreement_checked(self):
    #     checkbox = self.find_element((By.XPATH, '//input[@id="personalAgreement"]'))
    #     return checkbox.is_selected()
    #
    # def is_mandatory_field_label_has_appeared(self):
    #     return self.is_exists((By.CSS_SELECTOR, '.base-checkbox__error_personalagreement'))