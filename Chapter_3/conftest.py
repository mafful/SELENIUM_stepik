import pytest
from selenium import webdriver


"""
Для фикстур можно задавать область покрытия фикстур.
Допустимые значения: “function”, “class”, “module”, “session”.
Соответственно, фикстура будет вызываться один раз для тестового метода,
один раз для класса, один раз для модуля или один раз для всех тестов,
запущенных в данной сессии. -  @pytest.fixture(scope="class")
"""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



"""
При описании фикстуры можно указать дополнительный
параметр autouse=True, который укажет, что фикстуру нужно запустить
для каждого теста даже без явного вызова:
"""
@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")
