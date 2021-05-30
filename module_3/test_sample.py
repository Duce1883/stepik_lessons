from selenium import webdriver
from selenium.webdriver.support.ui import Select

# VARIABLES
locales = {
    'ru': 'ru',
    'en': 'en-gb',
}
main_page_link = 'http://selenium1py.pythonanywhere.com/ru/'
language_block_selector = '#language_selector'
language_block_select_selector = 'select[name="language"]'
language_block_button_selector = f'{language_block_selector} button[type="submit"]'
login_link_selector = '#login_link'
basket_block_selector = '.basket-mini'
store_nav_selector = '#browse'
store_search_form = f'.navbar-form[action="/{locales["ru"]}/search/"]'


def test_main_page_layout():
    browser = webdriver.Chrome()

    try:
        browser.implicitly_wait(10)
        browser.get(main_page_link)
        assert browser.find_element_by_css_selector(language_block_selector), "Can't find language switcher block"
        assert browser.find_element_by_css_selector(language_block_select_selector), "Can't find language switcher " \
                                                                                     "select element"
        assert browser.find_element_by_css_selector(
            language_block_button_selector), "Can't find language switcher submit button"
        assert browser.find_element_by_css_selector(login_link_selector), "Can't find login link"
        assert browser.find_element_by_css_selector(basket_block_selector), "Can't find basket block"
        assert browser.find_element_by_css_selector(store_nav_selector), "Can't find store navigation"
        assert browser.find_element_by_css_selector(store_search_form), "Can't find store search form"
    finally:
        browser.quit()


def test_default_locale():
    browser = webdriver.Chrome()
    try:
        browser.implicitly_wait(10)
        browser.get(main_page_link)
        locale = get_current_locale(browser)
        select = Select(browser.find_element_by_css_selector(language_block_select_selector))
        selected_option_val = get_current_selected_option_value(select)
        assert selected_option_val == locale, f"Language in URL({locale}) and selected language " \
                                              f"({selected_option_val}) does not match "
    finally:
        browser.quit()


def test_en_language_switching():
    browser = webdriver.Chrome()

    try:
        test_locale = locales['en']

        # ARRANGE
        browser.implicitly_wait(10)
        browser.get(main_page_link)

        # ACT
        select = Select(browser.find_element_by_css_selector(language_block_select_selector))
        select.select_by_value(test_locale)
        language_block_button = browser.find_element_by_css_selector(language_block_button_selector)
        language_block_button.click()

        # ASSERT
        select = Select(browser.find_element_by_css_selector(language_block_select_selector))
        selected_option_val = get_current_selected_option_value(select)
        assert selected_option_val == get_current_locale(browser), 'Language in URL has not switched'
        assert selected_option_val == test_locale, 'Wrong language was set in URL'

    finally:
        browser.quit()


def get_current_locale(browser):
    url_path = browser.execute_script('return window.location.pathname')
    url_path_parts = url_path.split('/')

    return url_path_parts[1]


def get_current_selected_option_value(select):
    selected_option = select.first_selected_option

    return selected_option.get_attribute("value")


test_main_page_layout()
test_default_locale()
test_en_language_switching()
