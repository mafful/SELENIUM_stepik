import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def calc(formula, x):
    x = float(x)  # Convert x to a float for computation
    if formula == "ln(abs(12*sin(x)))":
        result = math.log(abs(12 * math.sin(x)))
    else:
        raise ValueError(f"Unsupported formula: {formula}")
    return str(result)


def find_result(browser):
    formula_element = browser.find_element(
        By.CSS_SELECTOR, ".container .form-group label:nth-child(1)"
    ).text
    selector_value = browser.find_element(By.ID, "input_value").text
    print(formula_element)
    if formula_element and selector_value:
        formula = formula_element.split(" ")[2].split(",")[0]
        result = calc(formula=formula, x=selector_value)
        result_input = browser.find_element(By.ID, "answer")
        result_input.send_keys(result)
    else:
        print("Error: formula and value elements did not found on the page.")


def alert_confirmation(browser):
    confirm = browser.switch_to.alert
    confirm.accept()


def get_alert_answer(browser):
    alert = browser.switch_to.alert
    answer = alert.text.split(": ")[1]
    time.sleep(2)
    alert.accept()
    return answer


def click_button(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
    button.click()


def browsing(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # first page
        click_button(browser=browser)
        print(browser.window_handles)

        # second page
        new_window = browser.window_handles[1]
        browser.switch_to.window(window_name=new_window)
        find_result(browser=browser)
        click_button(browser=browser)
        answer = get_alert_answer(browser)
        print(answer)

    except NoSuchElementException as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(3)
        browser.quit()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/redirect_accept.html"
    browsing(link)
