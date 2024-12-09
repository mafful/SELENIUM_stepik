import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson_1_6_1_заполнение_формы import fill_in_form, data


url = "http://suninjuly.github.io/find_link_text"
searching_link = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser = webdriver.Chrome()
    browser.get(url)

    link = browser.find_element(By.LINK_TEXT, searching_link)
    print(searching_link)
    time.sleep(5)
    link.click()

    fill_in_form(browser=browser, link=link, data=data)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

except Exception as e:
    print(f"Error : {e}")

finally:
    time.sleep(5)
    browser.quit()
