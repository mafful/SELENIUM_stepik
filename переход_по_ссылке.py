
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Настроим драйвер и откроем страницу
driver = webdriver.Chrome()

# Функция для клика по ссылке и ожидания устаревания элемента
def click_through_to_new_page(link_text):
    # Находим ссылку по тексту и кликаем по ней
    link = driver.find_element(By.LINK_TEXT, link_text)
    link.click()

    # Функция для проверки, стал ли элемент устаревшим
    def is_stale(link):
        try:
            link.find_elements(By.ID, 'doesnt-matter')  # Пытаемся найти несуществующий элемент внутри
            return False  # Элемент еще существует
        except StaleElementReferenceException:
            return True  # Элемент устарел

    # Ожидаем, пока элемент не станет устаревшим
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: is_stale(link))

# Открываем веб-страницу
driver.get("http://example.com")  # Замените на реальный URL

# Используем нашу функцию для клика по ссылке и ожидания перехода
click_through_to_new_page("my link")  # Замените на текст ссылки, по которой нужно кликнуть

# Ожидаем появления нового элемента на странице
wait = WebDriverWait(driver, 10)
new_element = wait.until(EC.visibility_of_element_located((By.ID, "new-element-id")))  # Замените на идентификатор нового элемента

print("Новый элемент стал видимым!")

# Закрываем браузер
driver.quit()
