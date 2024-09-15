import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #@allure.step('Переход на нужный URL и открытие браузера на весь экран')
    #def navigate(self,url):
        #self.driver.get(url)
        #self.driver.fullscreen_window()

    @allure.step('Находим элемент')
    def find_element(self, locator,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден за {timeout} секунд.')
            return None

    @allure.step('Кликаем на элемент')
    def click_element(self, locator,timeout=10):
        element = self.find_element(locator,timeout)
        if element:
            element.click()
        else:
            pytest.fail(f'Не получилось кликнуть на элемент с локатором {locator}')

    @allure.step('Вводим текст в поле')
    def enter_text(self,locator,text,timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Не получилость ввести текст в элемент с локатором {locator}')
    @allure.step('Возвращаем текст на элементе')
    def get_text_of_element(self,locator,timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
    @allure.step('Прокручиваем страницу до нужного элемента')
    def scroll_to_element(self,locator,timeout=10):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator,timeout))
    @allure.step('Ожидаем видимость элемента')
    def wait_for_element_visible(self,locator,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print (f'Элемент с локатором {locator} не видим на протяжении {timeout} секунд.')
            return None
    @allure.step('Ожидаем присуствие элемента на странице')
    def element_is_present(self,locator,timeout=10):
        try:
            WebDriverWait(self.driver,timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False



