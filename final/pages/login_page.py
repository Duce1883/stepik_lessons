from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        # реализуйте проверку на корректный url адрес
        current_page_url = browser.current_url
        assert LoginPageLocators.LOGIN_URL in current_page_url, "Wrong page url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REG_FORM_EMAIL_SELECTOR)
        password_field = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REG_FORM_PASSWORD_SELECTOR)
        password_confirm_field = self.browser.find_element(By.CSS_SELECTOR,
                                                           LoginPageLocators.REG_FORM_PASSWORD_CONFIRM_SELECTOR)
        confirm_button = self.browser.find_element(By.CSS_SELECTOR, LoginPageLocators.REG_FORM_CONFIRM_BUTTON_SELECTOR)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        confirm_button.click()
