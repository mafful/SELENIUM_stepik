
import pytest
import faker

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .logger import logger
from utilities_browsing import time_to_see


# Fixture to provide the same link to all tests
@pytest.fixture
def product_link():
    return "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.fixture
def new_fake_user():
    f = faker.Faker()
    email = f.email()
    password = f.password(9)
    logger.info(f'{email}, {password}')
    return (email, password)


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, new_fake_user):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(*new_fake_user)



    def test_guest_cant_see_success_message(self, browser, product_link):
        page = ProductPage(
            browser, product_link
        )
        page.open()
        page.should_not_be_success_message()


    def test_guest_can_add_product_to_basket(self, browser, product_link):
        page = ProductPage(
            browser, product_link
        )
        page.open()
        page.looking_for_add_to_basket_button()
        ordering_book_title = page.ordering_book_title()
        ordering_book_price = page.ordering_book_price()
        page.add_to_basket()
        time_to_see(2)

        page.solve_quiz_and_get_code()

        page.view_basket()
        page.check_adding_book_title(expected_title=ordering_book_title)
        page.check_adding_book_price(expected_price=ordering_book_price)
        time_to_see(3)





@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    time_to_see(3)

@pytest.mark.skip
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

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    time_to_see(3)

    page.view_basket()
    logger.info("Moved to basket page...")

    page = BasketPage(browser, browser.current_url)
    page.should_not_be_basket_items()
    logger.info("Basket is empty!")
    time_to_see(5)