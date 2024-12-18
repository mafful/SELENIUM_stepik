import pytest

from .pages.product_page import ProductPage
from .logger import logger
from utilities_browsing import time_to_see

# Fixture to provide the same link to all tests
@pytest.fixture
def product_link():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(
        browser, product_link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    logger.info(f"Opening main page {product_link}...")
    page.open()
    logger.info("Main page opened successfully.")

    page.add_to_basket()
    logger.info("Add to basket button clicked.")

    page.should_not_be_success_message()
    logger.info("Success message is NOT presented")


def test_guest_cant_see_success_message(browser, product_link):
    page = ProductPage(
        browser, product_link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    logger.info(f"Opening main page {product_link}...")
    page.open()
    logger.info("Main page opened successfully.")

    page.should_not_be_success_message()
    logger.info("Success message is NOT presented")


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(
        browser, product_link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    logger.info(f"Opening main page {product_link}...")
    page.open()
    logger.info("Main page opened successfully.")

    page.add_to_basket()
    logger.info("Add to basket button clicked.")

    page.should_disappear_within_certain_time()
    logger.info("Success message has disappeared")
