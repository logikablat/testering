import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenCartPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_home_page(self):
        self.driver.get('https://demo.opencart-ru.ru/')
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        time.sleep(1.5)

    def click_element(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()
        time.sleep(1)

    def input_text(self, by, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, locator))
        )
        element.clear()
        element.send_keys(text)
        time.sleep(0.5)

    def back(self):
        self.driver.back()
        time.sleep(1.5)


@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    service = webdriver.chrome.service.Service('D:/allure-report-main/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def opencart_page(browser):
    return OpenCartPage(browser)


@allure.step("Нажать на элемент")
def step_click_element(page, by, locator):
    page.click_element(by, locator)


@allure.step("Ввести текст")
def step_input_text(page, by, locator, text):
    page.input_text(by, locator, text)


@allure.step("Вернуться назад")
def step_back(page):
    page.back()


@allure.title("Тест регистрации, авторизации и оформления заказа")
@allure.description("Тест проверяет регистрацию, авторизацию и успешное оформление заказа.")
def test_registration_login_and_checkout(opencart_page):
    with allure.step("Открытие главной страницы"):
        opencart_page.navigate_to_home_page()

    with allure.step("Нажатие на 'Личный кабинет'"):
        step_click_element(opencart_page, By.XPATH, "//span[contains(text(),'Личный кабинет')]")

    with allure.step("Открытие страницы регистрации"):
        step_click_element(opencart_page, By.XPATH, "//a[contains(text(),'Регистрация')]")

    with allure.step("Заполнение формы регистрации"):
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-firstname']", "логика")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-lastname']", "blat")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-email']", "logikablat0091@gmail.com")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-telephone']", "88005252525")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-password']", "11111geg")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-confirm']", "11111geg")

    with allure.step("Принятие соглашения и завершение регистрации"):
        step_click_element(opencart_page, By.XPATH, "//input[@name='agree']")
        step_click_element(opencart_page, By.XPATH, "//input[@value='Продолжить']")

    with allure.step("Возврат на главную страницу после регистрации"):
        opencart_page.navigate_to_home_page()

    with allure.step("Нажатие на 'Личный кабинет'"):
        step_click_element(opencart_page, By.XPATH, "//span[contains(text(),'Личный кабинет')]")

    with allure.step("Ввод email и пароля"):
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-email']", "logikablat0091@gmail.com")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-password']", "11111geg")

    with allure.step("Нажатие кнопки 'Войти'"):
        step_click_element(opencart_page, By.XPATH, "//input[@value='Войти']")

    with allure.step("Возврат на главную страницу после входа"):
        opencart_page.navigate_to_home_page()

    with allure.step("Нажатие на продукт"):
        step_click_element(opencart_page, By.XPATH, "//div[@class='product-layout product-grid swiper-slide swiper-slide-active']//div[@class='image']//a")

    with allure.step("Нажатие кнопки 'Купить'"):
        step_click_element(opencart_page, By.XPATH, "//button[@id='button-cart']")

    with allure.step("Нажатие на 'Оформление заказа'"):
        step_click_element(opencart_page, By.XPATH, "//a[contains(text(),'Оформление заказа')]")

    with allure.step("Заполнение данных для оплаты"):
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-payment-firstname']", "логика")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-payment-lastname']", "blat")
        step_input_text(opencart_page, By.XPATH, "//input[@id='input-payment-telephone']", "88005252525")
        step_click_element(opencart_page, By.XPATH, "//button[@id='button-payment-method']")

    with allure.step("Возврат на главную страницу"):
        opencart_page.navigate_to_home_page()  # Возврат на главную страницу вместо повторного нажатия "Купить".

    with allure.step("Нажатие на 'О нас'"):
        step_click_element(opencart_page, By.XPATH, "//a[@class='menu_main'][contains(text(),'О нас')]")

    with allure.step("Нажатие на 'Отзывы'"):
        step_click_element(opencart_page, By.XPATH, "//a[contains(text(),'Отзывы')]")

    with allure.step("Нажатие на 'Контакты'"):
        step_click_element(opencart_page, By.XPATH, "//a[contains(text(),'Контакты')]")


if __name__ == "__main__":
    pytest.main(args=['-s', '--alluredir', 'D:/allure-report-main/allure-results'])

