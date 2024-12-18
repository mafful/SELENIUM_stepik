# in terminal: pytest -s -v --tb=line --language=en Chapter_4/test_main_page.py
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .logger import logger
from utilities_browsing import time_to_see

# @pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    logger.info(f"Opening main page {link}...")
    page.open()                                  # открываем страницу
    logger.info("Main page opened successfully.")

    logger.info("Checking for login link...")
    page.should_be_login_link()
    logger.info("Login link is present.")

    logger.info("Getting login URL...")
    login_url = page.get_login_url()
    logger.info(f"Login URL obtained: {login_url}")

    time_to_see(5)
    logger.info("Navigating to login page...")
    page.go_to_login_page()

    login_page = LoginPage(browser, login_url)
    logger.info("Verifying login page...")
    login_page.should_be_login_url()
    logger.info("Login page URL is correct.")

    login_page.should_be_login_form()
    logger.info("Login form is present.")

    login_page.should_be_register_form()
    logger.info("Register form is present.")

    time_to_see(5)
    logger.info("Test passed: Guest can navigate to the login page successfully.")


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time_to_see(3)

    page.view_basket()
    logger.info("Moved to basket page...")

    page = BasketPage(browser, browser.current_url)
    page.should_not_be_basket_items()
    logger.info("Basket is empty!")
    time_to_see(5)

