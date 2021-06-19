from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_add_to_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), "Add to basket form is not presented"

    def should_be_add_to_basket_form_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_FORM_BUTTON), "Add to basket form button is not presented"

    def add_to_basket_form_button_click(self):
        button = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.ADD_TO_BASKET_FORM_BUTTON_SELECTOR)
        button.click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def get_product_name(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_NAME)

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def get_product_price(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)

    def should_be_alert_success(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG_PRODUCT_NAME), "Success message is not presented"

    def get_alert_success_product_name(self):
        return self.get_element_text(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG_PRODUCT_NAME)

    def should_be_alert_basket_info(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_INFO_MSG_PRICE), "Basket info  message is not presented"

    def get_alert_basket_price(self):
        return self.get_element_text(*ProductPageLocators.BASKET_INFO_MSG_PRICE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG_PRODUCT_NAME), \
            "Success message is not disappeared, but expected to be"
