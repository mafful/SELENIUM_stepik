import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from faker import Faker


def generate_data(number):
    fake = Faker()
    data = []
    for _ in range(number):
        # Generate specific fields
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        data.append((first_name, last_name, email))  # Append as a tuple
    return data


def fill_in_form(browser, file_path):
    form_element = browser.find_element(By.CSS_SELECTOR, "form")
    first_name = form_element.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    last_name = form_element.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    email = form_element.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    required_fields = (first_name, last_name, email)

    load_file_field = form_element.find_element(By.CSS_SELECTOR, 'input[type="file"]')

    generated_data = generate_data(1)
    # Flatten the list of tuples into a single list
    data = [item for sublist in generated_data for item in sublist]

    # Ensure you have enough data for required fields
    if len(data) < len(required_fields):
        raise ValueError("Not enough generated data for all required fields!")

    for i, required_field in enumerate(required_fields):
        required_field.send_keys(data[i])

    load_file_field.send_keys(file_path)


def click_button(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def browsing(link, FILE_PATH):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_in_form(browser=browser, file_path=FILE_PATH)
        click_button(browser)

    except NoSuchElementException as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    BASE_DIR = os.getcwd()
    FILE_PATH = os.path.join(BASE_DIR, "Chapter_2/test.txt")

    link = "http://suninjuly.github.io/file_input.html"
    browsing(link=link, FILE_PATH=FILE_PATH)
