import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:
    name_field = [By.XPATH,".//input[contains(@placeholder,'Имя')]"]
    surname_field = [By.XPATH,".//input[contains(@placeholder, 'Фамилия')]"]
    adress_field = [By.XPATH,".//input[contains(@placeholder, 'Адрес')]"]
    phone_number_field = [By.XPATH,".//input[contains(@placeholder, 'Телефон')]"]
    next_button = [By.XPATH, ".//button[text()='Далее']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу ЯндексСамокат')
    def fill_in_name_field(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Заполняем поле с именем пользователя')
    def fill_in_surname_field(self,surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Заполняем поле с фамилией пользователя')
    def fill_in_adress_field(self,adress):
        self.driver.find_element(*self.adress_field).send_keys(adress)

    @allure.step('Заполняем поле с телефоном пользователя')
    def fill_in_phone_field(self,phone):
        self.driver.find_element(*self.phone_number_field).send_keys(phone)

    @allure.step('Заполняем все поля о пользователе')
    def fill_in_all_fields_on_order_page_except_metro(self,name,surname,adress,phone):
        self.fill_in_name_field(name)
        self.fill_in_surname_field(surname)
        self.fill_in_adress_field(adress)
        self.fill_in_phone_field(phone)

    @allure.step('Кликаем на кнопку далее')
    def click_on_next_button(self):
        self.driver.find_element(*self.next_button).click()



class MetroLocators:
    metro_input = By.XPATH, "//input[@class='select-search__input']"
    def __init__(self, driver):
        self.driver = driver
    @staticmethod
    def get_metro_station_locator(metro):
        return By.XPATH, f"//*[@class='select-search__select']//*[text()='{metro}']"

    @allure.step('Заполняем поле со станцией метро')
    def fill_in_metro_station(self,metro):
        self.driver.find_element(*self.metro_input).send_keys(metro)

    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self,metro):
        self.driver.find_element(*MetroLocators.get_metro_station_locator(metro)).click()