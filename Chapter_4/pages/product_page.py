from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def looking_for_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ), "Add to basket button is not presented"

    def ordering_book_title(self):
        book_element = self.browser.find_element(
            *ProductPageLocators.ORDERING_BOOK_TITLE
        )
        return book_element.text

    def ordering_book_price(self):
        price_element = self.browser.find_element(
            *ProductPageLocators.ORDERING_BOOK_PRICE
        )
        price = price_element.text.replace("£", "").strip()
        return price

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_btn.click()

    def check_title_being_added(self, expected_title):
        title_being_added = self.browser.find_element(
            *ProductPageLocators.ALERT_ADDED_TITLE
        )
        assert title_being_added.text == expected_title

    def view_basket(self):
        view_basket_btn = self.browser.find_element(
            *ProductPageLocators.VIEW_BASKET_BUTTON
        )
        view_basket_btn.click()

    def check_adding_book_title(self, expected_title):
        book_element = self.browser.find_element(*ProductPageLocators.ADDING_BOOK_TITLE)
        assert book_element.text == expected_title

    def check_adding_book_price(self, expected_price):
        price_element = self.browser.find_element(
            *ProductPageLocators.ADDING_BOOK_PRICE
        )
        price = price_element.text.replace("£", "").strip()
        assert price == expected_price
