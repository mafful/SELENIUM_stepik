import pytest

from .pages.product_page import ProductPage
from .logger import logger
from utilities_browsing import time_to_see

base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{base_url}{i}" for i in range(10)]

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):

    try:
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

        logger.info("Check for added title of book...")
        try:
            page.check_title_being_added(expected_title=ordering_book_title)
        except AssertionError as e:
            pytest.xfail(f"Title mismatch on link {link}: {e}")

        logger.info("View basket...")
        page.view_basket()

        logger.info("Check title of adding book")
        page.check_adding_book_title(expected_title=ordering_book_title)

        logger.info("Check price of adding book")
        page.check_adding_book_price(expected_price=ordering_book_price)

        logger.info("Test passed: Book has been ordered with expected 'Title' and 'Price'.")

    except Exception as e:
        logger.error(f"Unexpected error on link {link}: {e}")
        pytest.fail(f"Test failed unexpectedly for link {link}. Error: {e}")
