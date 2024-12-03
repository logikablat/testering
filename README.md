# Отчет Allure

Этот репозиторий содержит пример теста Selenium с использованием библиотеки Allure для генерации отчетов о выполнении тестов.

## Установка зависимостей

Для запуска теста вам потребуются следующие зависимости:

- Python
- pytest
- selenium
- allure-pytest

Вы можете установить их с помощью следующей команды:

```bash
pip install pytest selenium allure-pytest
```
```bash
pip install selenium
```
```bash
pip install pytest
```

Запуск

```bash
python -m pytest D:\allure-report-main\mazila.py -s --alluredir=allure-results
```
