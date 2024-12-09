import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


def calc(x, sign, y):
    # Convert x and y to integers
    x = int(x)
    y = int(y)

    # Perform the calculation based on the operator
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    elif sign == "/":
        # Avoid division by zero
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
    else:
        raise ValueError(f"Unsupported operator: {sign}")


def find_result(browser):
    x = browser.find_element(By.ID, "num1").text
    sign = browser.find_element(By.CSS_SELECTOR, ".nowrap:nth-child(3)").text
    y = browser.find_element(By.ID, "num2").text
    if x and sign and y:
        result = str(calc(x=x, sign=sign, y=y))
        select = Select(browser.find_element(By.TAG_NAME, "select"))
        answer = select.select_by_value(result)
        print(f"Selected the result {answer} in the dropdown.")
    else:
        print("Error: Missing values to calculate the result.")


def click_button(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def browsing(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        find_result(browser)
        time.sleep(3)
        click_button(browser)

    except NoSuchElementException as e:
        print(f"Error finding form element: {e}")

    finally:
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/selects1.html"
    browsing(link)
