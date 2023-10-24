from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@id='top-s']")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Войти']")
    STATIC_BOOKS_MENU = (By.XPATH, "//ul[@id='staticmenu_body_books']")
    BOOKS_CONTAINER_GRID_PIN = (By.XPATH, "//div[@id= 'category_goods_container_books' and @class = 'b-main-pgs h-mpgs-grid-1']")
    BOOKS_CONTAINER_GRID_NOPIN = (
    By.XPATH, "//div[@id= 'category_goods_container_books' and @class = 'b-main-pgs h-mpgs-grid-1 mpgs-nopin']")


class SearchPageLocators:
    EMPTY_SEARCH_RESULTS = (By.XPATH, "//p[text() = 'Проверьте написан ли запрос без ошибок, или уменьшите количество слов в запросе.']")
    SHOW_FILTER_BY_PRICE_RESULTS_LINK = (By.CSS_SELECTOR, "a[id = 'f-results-link']")

class LoginPageLocators:
    EMAIL_LOGIN_GROUP_LINK = (By.XPATH, "//a[@id = 'loginFormLoginEmailLink']")
    PHONE_LOGIN_GROUP_LINK = (By.XPATH, "//a[@id = 'loginFormLoginPhoneLink']")
    # PHONE_LOGIN_GROUP_LINK = (By.CSS_SELECTOR, "a[@data-tab-link = 'phone']")
    EMAIL_INPUT = (By.XPATH, "//div[@class = 'i-input-group__cell']//input[@type = 'email']")
    PASSWORD_INPUT = (By.XPATH, "//div[@class = 'i-input-group__cell']//input[@type = 'password' and @class = 'i-input i-input_full-width i-input_with-padding i-popup__input']")
    ENTER_BUTTON = (By.XPATH, "//button[@value='login' and text()='Войти']")
    SEND_SMS_BUTTON = (By.XPATH, "//button[contains( text(),'Получить SMS')]")
    ENTER_BUTTON_AFTER_ERROR = (By.XPATH, "//button[@value='login' and text()='Войти' and @class = 'i-button i-button_full-width i-button_large i-button_primary i-popup__form-button i-button_disabled']")