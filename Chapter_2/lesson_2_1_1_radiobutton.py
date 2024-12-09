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


def checkbox_radiobutton_click(browser):
    robotCheckbox_label = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robotCheckbox_input = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox_label.click()
    robotCheckbox_checked = robotCheckbox_input.get_attribute("checked")

    robotsRule_label = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robotsRule_input = browser.find_element(By.ID, "robotsRule")
    robotsRule_label.click()
    robotsRule_checked = robotsRule_input.get_attribute("checked")

    if robotCheckbox_checked == "true" and robotsRule_checked == "true":
        print("Success: Checkbox and radio button are both selected!")
    else:
        error_message = "ERROR: Checkbox or radio button is not selected!"
        print(error_message)
        raise AssertionError(error_message)


def find_result(browser):
    formula_element = browser.find_element(By.CSS_SELECTOR, ".form-group .nowrap").text
    selector_value = browser.find_element(By.ID, "input_value").text

    if formula_element and selector_value:
        formula = formula_element.split(" ")[2].split(",")[0]
        result = calc(formula=formula, x=selector_value)
        result_input = browser.find_element(By.ID, "answer")
        result_input.send_keys(result)

        checkbox_radiobutton_click(browser=browser)
        time.sleep(3)
    else:
        print("Error: formula and value elements did not found on the page.")


def click_button(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def browsing(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        find_result(browser)
        click_button(browser)
        time.sleep(3)

    except NoSuchElementException as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    link = "https://suninjuly.github.io/math.html"
    browsing(link)
