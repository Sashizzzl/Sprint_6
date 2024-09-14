import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Url

class MainPage:
    order_button_in_header = [By.XPATH, './/div[contains(@class,"Header")]/button[text()="Заказать"]']
    order_button_in_home_area =[By.XPATH, ".// div[contains( @ class, 'Home')] / button[text()='Заказать']"]
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу ЯндексСамокат')
    def open_page(self):
        self.driver.get(Url.samokat_url)
        self.driver.fullscreen_window()

    @allure.step('Кликаем на кнопку заказа в верхней части страницы')
    def click_order_button_in_header(self):
        self.driver.find_element(*self.order_button_in_header).click()

    @allure.step('Пролистываем до нижней части страницы')
    def scroll_to_home_area(self):
        element = self.driver.find_element(*self.order_button_in_home_area)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем на кнопку заказа в нижней части страницы')
    def click_on_order_button_in_home_area(self):
        self.driver.find_element(*self.order_button_in_home_area).click()

