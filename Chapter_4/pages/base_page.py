import math

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators
from ..logger import logger


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(driver=self.browser, timeout=timeout).until(
                method=EC.presence_of_element_located(locator=(how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(
                driver=self.browser,
                timeout=timeout,
                poll_frequency=1,
                ignored_exceptions=TimeoutException,
            ).until_not(method=EC.presence_of_element_located(locator=(how, what)))
        except TimeoutException:
            return False
        return True

    def get_choosing_language(self):
        choosing_lang = self.browser.find_element(*BasePageLocators.CHOOSING_LANGUAGE)
        return choosing_lang.get_attribute("value")

    def should_be_authorized_user(self):
        user_authorised_locator = (
            BasePageLocators.USER_ICON[0],
            BasePageLocators.USER_ICON[1].format(self.get_choosing_language()),
        )
        assert self.is_element_present(*user_authorised_locator), (
            "User icon is not presented," " probably unauthorised user"
        )

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def get_login_url(self):
        login_link_element = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        return login_link_element.get_attribute("href")

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def view_basket(self):
        basket_button_locator = (
            BasePageLocators.VIEW_BASKET_BUTTON[0],
            BasePageLocators.VIEW_BASKET_BUTTON[1].format(self.get_choosing_language()),
        )
        view_basket_btn = self.browser.find_element(*basket_button_locator)
        view_basket_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        print(x)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            logger.error("No second alert presented")
