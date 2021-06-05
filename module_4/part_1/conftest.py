import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LANG = {"ru": "ru", "en-gb": "en-gb", "es": "es", "fr": "fr"}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help='There is only russian, english, spanish and french languages supported')


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
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
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
