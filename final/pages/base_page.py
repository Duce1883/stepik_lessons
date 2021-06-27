from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
import math
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_element_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element.text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_search_field(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_FIELD), "Search field is not presented"

    def should_be_search_button(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_BUTTON_EN), "Search button is not presented"

    def search_product_by_given_text(self, text):
        field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        field.click()
        field.send_keys(text)
        button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON_EN)
        button.click()

    def should_be_search_results_header(self):
        assert self.is_element_present(
            *BasePageLocators.SEARCH_RESULTS_HEADER), "Search results header is not presented"

    def should_search_results_header_has_right_text(self, expected_text='Products matching'):
        elem = self.browser.find_element(*BasePageLocators.SEARCH_RESULTS_HEADER)
        text = elem.text
        assert expected_text in text, "Wrong search results header"

    def should_be_breadcrumbs(self):
        assert self.is_element_present(
            *BasePageLocators.BREADCRUMBS), "Breadcrumbs is not presented"

    def should_be_sort_select(self):
        assert self.is_element_present(
            *BasePageLocators.SORT_SELECT), "Sort select is not presented"

    def should_be_browse_menu(self):
        assert self.is_element_present(
            *BasePageLocators.BROWSE_MENU), "Browse menu is not presented"

    def should_be_general_catalogue_link(self, link):
        assert self.is_element_present(
            *BasePageLocators.BROWSE_MENU_FIRST_BUTTON), "Browse general catalogue link button is not presented"
        elem = self.browser.find_element(*BasePageLocators.BROWSE_MENU_FIRST_BUTTON)
        href = elem.get_attribute("href")
        assert link in href, f'General catalogue link has wrong "href". Must be {link} in {href}'

    def click_on_general_catalogue_link(self):
        elem = self.browser.find_element(*BasePageLocators.BROWSE_MENU_FIRST_BUTTON)
        elem.click()

    def should_catalogue_header_has_right_text(self, expected_text='All products'):
        elem = self.browser.find_element(*BasePageLocators.SEARCH_RESULTS_HEADER)
        text = elem.text
        assert text == expected_text, "Wrong catalogue header"

    def click_on_offers_link(self):
        elem = self.browser.find_element(*BasePageLocators.BROWSE_MENU_LAST_BUTTON)
        elem.click()

    def should_be_special_sales_offer(self):
        assert self.is_element_present(
            *BasePageLocators.SPECIAL_SALES_OFFERS), "Special sales offers block is not presented"
