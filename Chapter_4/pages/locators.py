from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CHOOSING_LANGUAGE = (By.CSS_SELECTOR, "select[name='language'] option[selected='selected']")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default[href='/{}/basket/']")
    USER_ICON = (By.CSS_SELECTOR, "a[href='/{}/accounts/'] .icon-user")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR,"#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR,"#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn.btn-lg.btn-primary.btn-add-to-basket",
    )
    ORDERING_BOOK_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ORDERING_BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ALERT_ADDED_TITLE = (By.CSS_SELECTOR, 'div.alertinner strong')
    ADDING_BOOK_TITLE = (By.CSS_SELECTOR, "h3 > a")
    ADDING_BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color.align-right")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")