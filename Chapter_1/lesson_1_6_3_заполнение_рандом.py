from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import random
import string


def generate_random_data(num_fields):
    """
    Generate a list of random strings with lengths between 2 and 4.

    :param num_fields: Number of random strings to generate.
    :return: List of random strings.
    """
    random_data = []
    for _ in range(num_fields):
        length = random.randint(2, 4)
        random_string = "".join(random.choices(string.ascii_letters, k=length))
        random_data.append(random_string)
    return random_data


def fill_in_form(browser, link):
    form_element = browser.find_element(By.CSS_SELECTOR, "form")
    input_fields = form_element.find_elements(By.CSS_SELECTOR, "input")

    # Generate random data based on the number of input fields
    data = generate_random_data(len(input_fields))

    if len(input_fields) >= len(data):
        for i, input_field in enumerate(input_fields):
            input_field.send_keys(data[i])
    else:
        print("Error: Not enough input fields found on the page.")


if __name__ == "__main__":
    link = "http://suninjuly.github.io/huge_form.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_in_form(browser, link)
        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        button.click()
    except Exception as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(10)
        browser.quit()
