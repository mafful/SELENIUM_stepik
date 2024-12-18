from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Basket items are presented, but should not be"
