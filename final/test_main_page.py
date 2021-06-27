import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # ARRANGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_basket_link()

        # ACT
        page.go_to_basket_page()
        new_page = BasketPage(browser, link)

        # ASSERT
        new_page.should_be_empty_basket()
        new_page.should_be_empty_basket_message()


@pytest.mark.personal_tests
class TestCatalogueInMainPage:
    def test_should_see_search_elements(self, browser):
        # ARRANGE
        page = MainPage(browser, link)

        # ACT
        page.open()

        # ASSERT
        page.should_be_search_field()
        page.should_be_search_button()

    def test_search_has_results(self, browser):
        search_text = "shellcoder's"
        # ARRANGE
        page = MainPage(browser, link)
        page.open()

        # ACT
        page.search_product_by_given_text(search_text)

        # ASSERT
        page.should_be_search_results_header()
        page.should_search_results_header_has_right_text()
        page.should_be_breadcrumbs()
        page.should_be_sort_select()

    def test_should_see_catalogue_link(self, browser, language):
        general_catalogue_link = f'/{language}/catalogue/'
        # ARRANGE
        page = MainPage(browser, link)

        # ACT
        page.open()

        # ASSERT
        page.should_be_browse_menu()
        page.should_be_general_catalogue_link(general_catalogue_link)

    def test_can_go_to_catalogue(self, browser):
        # ARRANGE
        page = MainPage(browser, link)
        page.open()

        # ACT
        page.click_on_general_catalogue_link()

        # ASSERT
        page.should_be_breadcrumbs()
        page.should_be_search_results_header()
        page.should_catalogue_header_has_right_text()

    @pytest.mark.xfail
    def test_can_see_special_sales_offers(self, browser):
        # ARRANGE
        page = MainPage(browser, link)
        page.open()

        # ACT
        page.click_on_offers_link()

        # ASSERT
        page.should_be_special_sales_offer()
