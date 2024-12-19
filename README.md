# STEPIK_selenium_course

Этот репозиторий хранит домашние работы по курсу “Автоматизация тестирования” на Stepik:
https://stepik.org/course/575.


### Чтобы запустить финальный тест:

1. Перейдите в директорию `Chapter_4`:
   ```bash
   cd Chapter_4
   ```

2.	Запустите финальный тест с помощью следующей команды:
    ```bash
    pytest -m "login or need_review" --language=fr
    ```
      или
      ```bash
      pytest -v --tb=line --language=en -m need_review
      ```
