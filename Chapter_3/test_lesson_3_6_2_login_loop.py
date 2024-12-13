import os
import math
import time

from dotenv import load_dotenv
import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


from utilities_browsing import (
    handle_modal_popup,
    wait_for_element_located,
    wait_for_element_located_and_visible,
    wait_for_element_to_be_clickable_and_visible,
    wait_for_element_to_disappear,
    time_to_see,
)

load_dotenv()


STEPIK_LOGIN = os.getenv("STEPIK_LOGIN")
STEPIK_PASSWORD = os.getenv("STEPIK_PASSWORD")

LESSON_NUMBERS = [
    236895,
    236896,
    236897,
    236898,
    236899,
    236903,
    236904,
    236905,
]

FINAL_ANSWER = []

# Generate full URLs from lesson numbers
LINKS = [
    f"https://stepik.org/lesson/{lesson_number}/step/1"
    for lesson_number in LESSON_NUMBERS
]


def proceed_with_login(browser):
    """Input credentials and submit the login form."""
    try:
        browser.find_element(By.NAME, "login").send_keys(STEPIK_LOGIN)
        browser.find_element(By.NAME, "password").send_keys(STEPIK_PASSWORD)
        print("Login and password filled ...")
        browser.find_element(
            By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader[type="submit"]'
        ).click()
        print("Login form submitted.")
        # # Check if login form disappears
        wait_for_element_to_disappear(browser, By.ID, "ember898", timeout=10)

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error during login process: {e}")


def stepik_login(browser, url):
    """Main test function to perform login."""
    link = url
    browser.get(link)

    # Wait for the login button to appear
    login_button = wait_for_element_to_be_clickable_and_visible(
        browser, By.ID, "ember471", timeout=10
    )
    if login_button:
        login_button.click()
        proceed_with_login(browser=browser)
    else:
        print("Login button not found, stopping test.")
        return


@pytest.mark.parametrize("url", LINKS)
def test_check_answer(browser, url):
    stepik_login(browser, url)
    time_to_see(5)

    try:
        again_button = browser.find_element(By.CSS_SELECTOR, "button.again-btn.white")
        if again_button:
            again_button.click()
            handle_modal_popup(browser)
    except NoSuchElementException:
        print("Again_button is not presented, continue...")

    answer_textarea = wait_for_element_located_and_visible(
        browser,
        By.CSS_SELECTOR,
        "textarea.ember-text-area.textarea.string-quiz__textarea",
    )
    print("Answer textarea exist...")
    answer = math.log(int(time.time()))
    answer_textarea.send_keys(f"{answer}")
    submit_button = wait_for_element_to_be_clickable_and_visible(
        browser, By.CSS_SELECTOR, "button.submit-submission"
    )
    if submit_button:
        submit_button.click()
    else:
        print("Submit button not clickable.")
    time_to_see(10)

    check_answer = wait_for_element_located(
        browser, By.CSS_SELECTOR, "p.smart-hints__hint", 2
    )
    if check_answer:
        if check_answer.text != "Correct!":
            print(check_answer.text)
            FINAL_ANSWER.append(check_answer.text)
    else:
        print("Button did not clicked properly, reload page...")
        browser.refresh()  # Optionally refresh the page
        test_check_answer(browser, url)  # Re-run the test for this URL

    print(f"Final Answer Feedback: {''.join(FINAL_ANSWER)}")
