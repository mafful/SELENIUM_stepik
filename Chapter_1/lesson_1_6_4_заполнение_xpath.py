from selenium import webdriver
from selenium.webdriver.common.by import By

import time


data = ["Ivan", "Petrov", "Smolensk", "Russia"]


def fill_in_form(browser, link, data):
    form_element = browser.find_element(By.CSS_SELECTOR, "form")
    input_fields = form_element.find_elements(By.CSS_SELECTOR, "input")

    if len(input_fields) >= len(data):
        for i, input_field in enumerate(input_fields):
            input_field.send_keys(data[i])
            time.sleep(0.1)
    else:
        print("Error: Not enough input fields found on the page.")


def click_button(browser):
    button = browser.find_element(
        By.XPATH, '//button[@class="btn" and text()="Submit"]'
    )
    button.click()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/find_xpath_form"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_in_form(browser, link, data)
        click_button(browser)

    except Exception as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(10)
        browser.quit()
