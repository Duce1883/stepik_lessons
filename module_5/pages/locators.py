from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_TO_BASKET_FORM_BUTTON_SELECTOR = "#add_to_basket_form button"
    ADD_TO_BASKET_FORM_BUTTON = (By.CSS_SELECTOR, ADD_TO_BASKET_FORM_BUTTON_SELECTOR)
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    ADD_TO_BASKET_SUCCESS_MSG_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_INFO_MSG_PRICE = (By.CSS_SELECTOR, ".alert-info p:first-child strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MSG = (By.XPATH, "//*[@id='content_inner']//*[contains(text(), 'Ваша корзина пуста')]")
