import math
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


FORMULA_PATTERN = r"ln\((.*)\)"


def calc(formula, x):
    x = float(x)  # Convert x to a float for computation
    if formula == "ln(abs(12*sin(x)))":
        result = math.log(abs(12 * math.sin(x)))
    else:
        raise ValueError(f"Unsupported formula: {formula}")
    return str(result)


def find_result(browser):
    formula_element = browser.find_element(
        By.CSS_SELECTOR, ".form-group label span.nowrap"
    ).text
    selector_value = browser.find_element(By.ID, "input_value").text

    if formula_element and selector_value:
        # Use regex to find the formula
        match = re.search(FORMULA_PATTERN, formula_element)
        if match:
            formula = match.group(0)
        result = calc(formula=formula, x=selector_value)
        result_input = browser.find_element(By.ID, "answer")
        result_input.send_keys(result)
    else:
        print("Error: formula and value elements did not found on the page.")


# Ожидание появления определенной цены
def booking(browser):
    while True:
        try:
            WebDriverWait(browser, 5).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "$100")
            )
            print("Price is now $100!")
            break  # Exit the loop if the price is $100
        except TimeoutException:
            print("Price hasn't reached $100 yet, checking again in a few seconds...")
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            break


# Экстракт ответ из алерта
def get_alert_answer(browser):
    alert = browser.switch_to.alert
    answer = alert.text.split(": ")[1]
    time.sleep(2)
    alert.accept()
    return answer


def browsing(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        booking(browser=browser)
        browser.find_element(By.ID, "book").click()

        find_result(browser)

        button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "solve"))
        )
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        time.sleep(3)

        answer = get_alert_answer(browser)
        print(answer)

    except NoSuchElementException as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    urls = [
        "http://suninjuly.github.io/explicit_wait2.html",
    ]
    for url in urls:
        print(f"Open up page {url}")
        browsing(url)
        print(f"Page {url} closed")
        time.sleep(5)
