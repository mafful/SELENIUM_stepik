import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def wait_for_element_located(browser, by, value, timeout=10):
    """Wait for an element to be present."""
    try:
        element = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Timeout: Element {value} not found within {timeout} seconds.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def wait_for_element_located_and_visible(browser, by, value, timeout=10, max_attempts=3):
    """Wait for an element to be present."""
    attempt = 0
    while attempt < max_attempts:
        try:
            print(f"Attempt {attempt + 1} to locate element '{value}'...")
            element = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Timeout: Element '{value}' not found within {timeout} seconds on attempt {attempt + 1}.")
            time.sleep(5)
            attempt += 1
        except Exception as e:
            print(f"An unexpected error occurred on attempt {attempt + 1}: {e}")
            attempt += 1
    print(f"Failed to locate element '{value}' after {max_attempts} attempts.")
    return None


def wait_for_element_to_be_clickable_and_visible(browser, by, value, timeout=10, max_attempts=3):
    """Wait for an element to be clickable and visible, with retry attempts."""
    attempt = 0
    while attempt < max_attempts:
        try:
            print(f"Attempt {attempt + 1} to locate element '{value}'...")
            # Wait for visibility
            element = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            # Wait for clickability
            element = WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except TimeoutException:
            print(f"Timeout: Element '{value}' not found within {timeout} seconds on attempt {attempt + 1}.")
            time.sleep(5)
            attempt += 1
        except Exception as e:
            print(f"An unexpected error occurred on attempt {attempt + 1}: {e}")
            attempt += 1
    print(f"Failed to locate element '{value}' after {max_attempts} attempts.")
    return None


def wait_for_element_to_disappear(browser, by, value, timeout=10):
    """Wait for an element to disappear."""
    try:
        WebDriverWait(browser, timeout).until_not(
            EC.presence_of_element_located((by, value))
        )
        print(f"Element {value} disappeared.")
        return True
    except TimeoutException:
        print(f"Timeout: Element {value} did not disappear within {timeout} seconds.")
        return False


def time_to_see(countdown: int=10):
    """Prints a countdown timer for the user to review the result."""
    print("Время на посмотреть и оценить результат!")
    print("Отсчет пошел...")
    for i in range(countdown):
        print(f"Осталось на просмотр - {countdown - i}")
        time.sleep(1)


def handle_modal_popup(browser):
    try:
        # Wait for the modal to appear
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-popup__container"))
        )
        print("Modal popup is visible.")

        # Find and click the "OK" button
        ok_button = browser.find_element(By.CSS_SELECTOR, 'footer.modal-popup__footer.ember-view > button:nth-of-type(1)')
        ok_button.click()
        print("Clicked 'OK' on the modal popup.")
    except (TimeoutException, NoSuchElementException):
        print("Modal popup did not appear.")
    except Exception as e:
        print(f"An error occurred while handling the modal: {e}")




