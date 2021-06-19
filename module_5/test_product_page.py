import time
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestProductPage():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_form_button_click()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_form_button_click()
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        prod_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, prod_link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        prod_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, prod_link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        prod_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, prod_link)
        page.open()
        page.should_be_basket_link()
        page.go_to_basket_page()
        new_page = BasketPage(browser, prod_link)
        new_page.should_be_empty_basket()
        new_page.should_be_empty_basket_message()


# @pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        page.should_be_register_form()
        reg_email = f'{str(time.time())}_randomail@fakemail.org'
        reg_password = 'p4ssw0rD8888'
        page.register_new_user(reg_email, reg_password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        # ARRANGE
        page = ProductPage(browser, link, timeout=5)
        page.open()
        page.should_be_product_name()
        page.should_be_product_price()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.should_be_add_to_basket_form()
        page.should_be_add_to_basket_form_button()

        # ACT
        page.add_to_basket_form_button_click()

        # ASSERT
        page.should_be_alert_success()
        page.should_be_alert_basket_info()
        alert_success_product_name = page.get_alert_success_product_name()
        alert_basket_price = page.get_alert_basket_price()
        assert product_name == alert_success_product_name, "Added product name doesn't match expected name"
        assert product_price == alert_basket_price, "Added product price doesn't match expected price"

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
