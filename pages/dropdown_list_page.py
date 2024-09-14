import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Url

class DropdownList:
    elements_of_list= [(By.ID, 'accordion__heading-0'),(By.ID, 'accordion__heading-1'),(By.ID, 'accordion__heading-2'),(By.ID, 'accordion__heading-3'), (By.ID, 'accordion__heading-4'), (By.ID, 'accordion__heading-5'), (By.ID, 'accordion__heading-6'), (By.ID, 'accordion__heading-7')]
    text_of_elements = [(By.ID, 'accordion__panel-0'),(By.ID, 'accordion__panel-1'),(By.ID, 'accordion__panel-2'),(By.ID, 'accordion__panel-3'), (By.ID, 'accordion__panel-4'), (By.ID, 'accordion__panel-5'), (By.ID, 'accordion__panel-6'), (By.ID, 'accordion__panel-7')]
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу ЯндексСамокат')
    def open_page(self):
        self.driver.get(Url.samokat_url)
    @allure.step('Пролистываем до выпадающего списка')
    def scroll_to_dropdown_list(self,item_index):
        element = self.driver.find_element(*self.elements_of_list[item_index])
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем кликабельности элемента списка')
    def wait_till_element_is_clickable(self,item_index):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.elements_of_list[item_index]))

    @allure.step('Кликаем по элементу выпадающего списка')
    def click_on_element_of_list(self,item_index):
        self.driver.find_element(*self.elements_of_list[item_index]).click()

    @allure.step('Получаем тест элемента выпадающего списка')
    def value_in_text_of_element(self,item_index):
        return self.driver.find_element(*self.text_of_elements[item_index]).text


