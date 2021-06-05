import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_user_registration(browser):
    login_link_selector = "#login_link"
    register_form_selector = "#register_form"
    messages_selector = '#messages'
    alert_success_selector = '.alert-success'

    browser.get(LINK)
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_link_selector)))
    login_link = browser.find_element_by_css_selector(login_link_selector)
    login_link.click()
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, register_form_selector)))

    fill_form(browser, register_form_selector)

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, messages_selector)))
    browser.find_element_by_css_selector(alert_success_selector)


def fill_form(browser, register_form_selector):
    register_form_email_selector = "#id_registration-email"
    register_form_pw_selector = "#id_registration-password1"
    register_form_confirm_pw_selector = "#id_registration-password2"
    pw = 'p4ssw0rD8888'
    submit_register_button_selector = f'{register_form_selector} button[type="submit"]'
    letters = string.ascii_lowercase
    email = f"{''.join(random.choice(letters) for i in range(10))}@randomail.so"

    register_form_email = browser.find_element_by_css_selector(register_form_email_selector)
    register_form_pw = browser.find_element_by_css_selector(register_form_pw_selector)
    register_form_confirm_pw = browser.find_element_by_css_selector(register_form_confirm_pw_selector)
    submit_register_button = browser.find_element_by_css_selector(submit_register_button_selector)

    register_form_email.send_keys(email)
    register_form_pw.send_keys(pw)
    register_form_confirm_pw.send_keys(pw)
    submit_register_button.click()
