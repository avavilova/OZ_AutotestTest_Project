import os

BASE_URL = 'https://www.oz.by/'


class TIMEOUTS:
    GET_URL = 20
    FIND_ELEMENT = 20

BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', True)

class HEADLESS_OPTION:
    CHROME_HEADLESS = '--headless=new'
    FIREFOX_HEADLESS = '--headless'

class BROWSER_NAME:
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    ALL = (CHROME, FIREFOX)

