import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["okay_offer",
                              pytest.param("bugged_offer", marks=pytest.mark.xfail),
                              "okay_offer"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # ARRANGE
        page = ProductPage(browser, link + promo_offer, timeout=5)
        page.open()
        page.should_be_product_name()
        page.should_be_product_price()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.should_be_add_to_basket_form()
        page.should_be_add_to_basket_form_button()

        # ACT
        page.add_to_basket_form_button_click()
        page.solve_quiz_and_get_code()

        # ASSERT
        page.should_be_alert_success()
        page.should_be_alert_basket_info()
        alert_success_product_name = page.get_alert_success_product_name()
        alert_basket_price = page.get_alert_basket_price()
        assert product_name == alert_success_product_name, "Added product name doesn't match expected name"
        assert product_price == alert_basket_price, "Added product price doesn't match expected price"
