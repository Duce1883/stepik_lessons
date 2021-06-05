from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

ADD_TO_BUTTON_EXPECTED_TEXT = {"ru": "Добавить в корзину", "en-gb": "Add to basket", "es": "Añadir al carrito",
                               "fr": "Ajouter au panier"}


def test_add_to_basket_button_text(browser, language):
    browser.get(LINK)

    add_to_basket_button_selector = ".btn-add-to-basket"
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, add_to_basket_button_selector)))
    add_to_basket_button = browser.find_element_by_css_selector(add_to_basket_button_selector)

    assert add_to_basket_button.text == ADD_TO_BUTTON_EXPECTED_TEXT[language], "Wrong text in 'add to basket' button"
