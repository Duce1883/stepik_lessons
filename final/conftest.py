import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

LANG = {"ru": "ru", "en-gb": "en-gb", "es": "es", "fr": "fr"}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help='There is only russian, english, spanish and french languages supported')


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language").lower()
    if language not in LANG:
        raise pytest.UsageError(f"--language should be one of: {', '.join(LANG)}")
    return language


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('screenshots/screenshot-%s.png' % now)
    browser.quit()
