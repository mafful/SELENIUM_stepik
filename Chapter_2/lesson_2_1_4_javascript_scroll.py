import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(3)
button = browser.find_element(By.TAG_NAME, "button")

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# - - - - -
# Для сравнения приведем скрипт на этом языке,
# который делает то же, что приведенный выше пример для WebDriver:

# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);

# попробовать исполнить его в консоли браузера
# на странице http://suninjuly.github.io/execute_script.html
# - - - - -

time.sleep(5)
button.click()

browser.quit()
