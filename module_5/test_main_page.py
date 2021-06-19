from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, language):
        page = MainPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.go_to_basket_page()
        new_page = BasketPage(browser, link)
        new_page.should_be_empty_basket()
        new_page.should_be_empty_basket_message()


class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page(browser)
