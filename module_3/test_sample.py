from selenium import webdriver
from selenium.webdriver.support.ui import Select

# VARIABLES
main_page_link = 'http://selenium1py.pythonanywhere.com/ru/'
language_block_selector = '#language_selector'
language_block_select_selector = 'select[name="language"]'
language_block_button_selector = f'{language_block_selector} button[type="submit"]'

browser = webdriver.Chrome()


def test_language_switching():
    locales = {
        'ru': 'ru',
        'en': 'en-gb',
    }

    expected_final_locale = locales['en']

    try:
        # ARRANGE
        browser.implicitly_wait(10)
        browser.get(main_page_link)

        assert browser.find_element_by_css_selector(language_block_selector), "Can't find language switcher block"
        assert browser.find_element_by_css_selector(language_block_select_selector), "Can't find language switcher " \
                                                                                     "select "
        assert browser.find_element_by_css_selector(
            language_block_button_selector), "Can't find language switcher submit button"
        start_locale = get_current_locale()
        select = Select(browser.find_element_by_css_selector(language_block_select_selector))
        selected_option_val = get_current_selected_option_value(select)
        assert selected_option_val == start_locale, f"Language in URL({start_locale}) and selected language " \
                                                    f"({selected_option_val}) does not match "

        # ACT
        if selected_option_val == locales['ru']:
            select.select_by_value(locales['en'])
        else:
            select.select_by_value(locales['ru'])
            expected_final_locale = locales['ru']
        language_block_button = browser.find_element_by_css_selector(language_block_button_selector)
        language_block_button.click()

        # ASSERT
        select = Select(browser.find_element_by_css_selector(language_block_select_selector))
        selected_option_val = get_current_selected_option_value(select)
        assert selected_option_val != start_locale, f"Language option has not changed"
        assert selected_option_val == expected_final_locale, f"Wrong language option selected"
        new_locale = get_current_locale()
        assert new_locale != start_locale, 'Language in URL has not switched'
        assert new_locale == expected_final_locale, 'Wrong language was set in URL'

    finally:
        browser.quit()


def get_current_locale():
    url_path = browser.execute_script('return window.location.pathname')
    url_path_parts = url_path.split('/')

    return url_path_parts[1]


def get_current_selected_option_value(select):
    selected_option = select.first_selected_option

    return selected_option.get_attribute("value")


test_language_switching()
