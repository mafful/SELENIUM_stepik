import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


data = ["Ivan", "Petrov", "root@admin.ru"]


def fill_in_form(browser, link, data):
    form_element = browser.find_element(By.CSS_SELECTOR, "form")
    required_fields = form_element.find_elements(By.CSS_SELECTOR, "input[required]")

    if len(required_fields) >= len(data):
        for i, required_field in enumerate(required_fields):
            required_field.send_keys(data[i])
            time.sleep(0.1)
    else:
        print("Error: Not enough input fields found on the page.")


def click_button(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def browsing(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_in_form(browser, link, data)
        time.sleep(2)
        click_button(browser)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    except NoSuchElementException as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/registration1.html"
    browsing(link)
    time.sleep(2)
    link = "http://suninjuly.github.io/registration2.html"
    browsing(link)
