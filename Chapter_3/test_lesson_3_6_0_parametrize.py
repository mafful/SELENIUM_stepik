import time

from typing import Literal
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("language", ["ru", "en-gb"])
def test_guest_should_see_login_link(
    browser: WebDriver, language: Literal["ru"] | Literal["en-gb"]
):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(3)
