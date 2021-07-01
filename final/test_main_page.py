import pytest
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    @pytest.mark.personal_tests
    @pytest.mark.parametrize('url',
                             ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
                              "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/",
                              "http://selenium1py.pythonanywhere.com/"])
    def test_can_see_language_selector(self, browser, url):
        # ARRANGE
        page = MainPage(browser, url)

        # ACT
        page.open()

        # ASSERT
        page.should_be_language_switcher()


class TestCatalogueInMainPage:
    @pytest.mark.personal_tests
    def test_should_see_search_elements(self, browser):
        # ARRANGE
        page = MainPage(browser, link)

        # ACT
        page.open()

        # ASSERT
        page.should_be_search_field()
        page.should_be_search_button()

    @pytest.mark.personal_tests
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

    @pytest.mark.personal_tests
    def test_should_see_catalogue_link(self, browser, language):
        general_catalogue_link = f'/{language}/catalogue/'
        # ARRANGE
        page = MainPage(browser, link)

        # ACT
        page.open()

        # ASSERT
        page.should_be_browse_menu()
        page.should_be_general_catalogue_link(general_catalogue_link)

    @pytest.mark.personal_tests
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
    @pytest.mark.personal_tests
    def test_can_see_special_sales_offers(self, browser):
        # ARRANGE
        page = MainPage(browser, link)
        page.open()

        # ACT
        page.click_on_offers_link()

        # ASSERT
        page.should_be_special_sales_offer()
