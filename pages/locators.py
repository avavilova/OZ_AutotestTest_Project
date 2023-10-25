from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@id='top-s']")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Войти']")
    STATIC_BOOKS_MENU = (By.XPATH, "//ul[@id='staticmenu_body_books']")
    BOOKS_CONTAINER_GRID_PIN = (
        By.XPATH, "//div[@id= 'category_goods_container_books']")
    BOOKS_CONTAINER_GRID_NOPIN = (
        By.XPATH, "//div[@id= 'category_goods_container_books']")


class SearchPageLocators:
    EMPTY_SEARCH_RESULTS = (
        By.XPATH, "//p[text() = 'Проверьте написан ли запрос без ошибок, или уменьшите количество слов в запросе.']")
    SHOW_FILTER_BY_PRICE_RESULTS_LINK = (By.CSS_SELECTOR, "a[id = 'f-results-link']")


class LoginPageLocators:
    EMAIL_LOGIN_GROUP_LINK = (By.XPATH, "//a[@id = 'loginFormLoginEmailLink']")
    PHONE_LOGIN_GROUP_LINK = (By.XPATH, "//a[@id = 'loginFormLoginPhoneLink']")
    EMAIL_INPUT = (By.XPATH, "//div[@class = 'i-input-group__cell']//input[@type = 'email']")
    PASSWORD_INPUT = (By.XPATH, "//div[@class = 'i-input-group__cell']//input[@type = 'password']")
    ENTER_BUTTON = (By.XPATH, "//button[@value='login' and text()='Войти']")
    SEND_SMS_BUTTON = (By.XPATH, "//button[contains( text(),'Получить SMS')]")
    PHONE_ERROR_MSG = (By.XPATH, "//div[text()='Введите номер мобильного телефона белорусских опереторов']")
    INCORRECT_PASSWORD_MSG = (By.XPATH, "//div[text()='Неверный пароль. Если вы потеряли или забыли пароль — ']")
    INCORRECT_EMAIL_MSG = (By.XPATH, "//div[@id = 'test']//div[text()='Введите корректный адрес электронной почты']")
