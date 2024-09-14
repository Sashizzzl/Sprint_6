import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AboutRentPage:
    time_field = [By.XPATH,".//input[contains(@placeholder,'Когда')]"]
    rental_period_field = [By.XPATH,".//span[@class='Dropdown-arrow']"]
    rental_period_one_day = [By.XPATH, ".//div[contains(@class,'Dropdown-option') and contains(text(),'сутки')]"]
    order_button = [By.XPATH,".//div[contains(@class, 'Order')]/button[text()='Заказать']"]
    button_yes_in_pop_up_do_you_want_to_order = [By.XPATH,".//button[text()='Да']"]
    order_is_placed = [By.XPATH,".//div[contains(@class,'Order_ModalHeader')]"]
    button_to_see_status_in_pup_up_order_is_placed = [By.XPATH, ".//button[text()='Посмотреть статус']"]
    samokat_logo = [By.XPATH, ".//img[@alt='Scooter']"]
    yandex_logo = [By.XPATH, ".//img[@alt='Yandex']"]
    find_button_on_yandex_page = (By.XPATH,".//button[text()='Найти']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поле со временем доставки')
    def fill_in_time_field(self, time):
        self.driver.find_element(*self.time_field).send_keys(time)

    @allure.step('Заполняем поле с периодом аренды')
    def click_on_rental_period_field(self):
        self.driver.find_element(*self.rental_period_field).click()

    @allure.step('Выбираем период аренды')
    def choose_rental_period_time(self):
        self.driver.find_element(*self.rental_period_one_day).click()

    @allure.step('Кликаем на кнопку заказать')
    def click_on_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Кликаем на кнопку заказать')
    def confirm_order(self):
        self.driver.find_element(*self.button_yes_in_pop_up_do_you_want_to_order).click()

    @allure.step('Заполняем все обязательные поля в окне заказа и подтверждаем заказ')
    def complete_order_in_rent_page(self,time):
        self.fill_in_time_field(time)
        self.click_on_rental_period_field()
        self.choose_rental_period_time()
        self.click_on_order_button()
        self.confirm_order()

    @allure.step('Получаем значение из окна подтверждения заказа')
    def value_in_confirmation_window(self):
        return self.driver.find_element(*self.order_is_placed).text

    @allure.step('Нажимаем на кнопку посмотреть статус')
    def click_on_see_status_in_confirmation_window(self):
        self.driver.find_element(*self.button_to_see_status_in_pup_up_order_is_placed).click()

    @allure.step('Клик на лого Самокат')
    def click_on_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()

    @allure.step('Клик на лого Яндекс')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url


