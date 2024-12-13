import os
import time
from typing import Literal

from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


from utilities_browsing import (
    wait_for_element_to_be_clickable,
    wait_for_element_to_disappear,
    time_to_see
)

load_dotenv()


STEPIK_LOGIN = os.getenv("STEPIK_LOGIN")
STEPIK_PASSWORD = os.getenv("STEPIK_PASSWORD")


def proceed_with_login(browser):
    """Input credentials and submit the login form."""
    try:
        browser.find_element(By.NAME, "login").send_keys(STEPIK_LOGIN)
        browser.find_element(By.NAME, "password").send_keys(STEPIK_PASSWORD)
        print("Login and password filled ...")
        time.sleep(5)
        browser.find_element(
            By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader[type="submit"]'
        ).click()
        print("Login form submitted.")

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error during login process: {e}")


def test_login(browser):
    """Main test function to perform login."""
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    # Wait for the login button to appear
    login_button = wait_for_element_to_be_clickable(
        browser, By.ID, "ember471", timeout=10
    )
    if login_button:
        login_button.click()
    else:
        print("Login button not found, stopping test.")
        return

    # Perform login
    proceed_with_login(browser)

    # Time to observe page after login
    time_to_see(countdown=5)

    # Check if login form disappears
    login_window = wait_for_element_to_disappear(browser, By.ID, "ember898", timeout=10)

    # Assert that the login window disappears
    assert login_window, "Login window did not disappear as expected."
    print("Test succeeded properly!")
