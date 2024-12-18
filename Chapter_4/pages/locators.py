from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn.btn-lg.btn-primary.btn-add-to-basket",
    )
    ORDERING_BOOK_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ORDERING_BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ALERT_ADDED_TITLE = (By.CSS_SELECTOR, 'div.alertinner strong')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "p > a.btn.btn-info:first-of-type")
    ADDING_BOOK_TITLE = (By.CSS_SELECTOR, "h3 > a")
    ADDING_BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color.align-right")
