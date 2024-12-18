from .pages.product_page import ProductPage
from .logger import logger
from utilities_browsing import time_to_see

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    time_to_see(3)


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(
        browser, link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    logger.info(f"Opening main page {link}...")
    page.open()
    logger.info("Main page opened successfully.")

    logger.info("Checking for adding to basket button...")
    page.looking_for_add_to_basket_button()
    logger.info("Add to basket button is present.")

    logger.info("Adding book ...")
    ordering_book_title = page.ordering_book_title()
    ordering_book_price = page.ordering_book_price()
    logger.info(
        f"Book '{ordering_book_title}' with a price of: '{ordering_book_price}£' has been choosen!"
    )

    page.add_to_basket()
    logger.info("Add to basket button clicked.")

    logger.info("Trying to solve quiz from alert window...")
    page.solve_quiz_and_get_code()
    logger.info("Quiz has been solved.")
    page.view_basket()

    logger.info("Check title of adding book")
    page.check_adding_book_title(expected_title=ordering_book_title)

    logger.info("Check price of adding book")
    page.check_adding_book_price(expected_price=ordering_book_price)

    time_to_see(3)
    logger.info("Test passed: Book has been ordered with expected 'Title' and 'Price'.")
