import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    NAME_FIELD = [By.XPATH,".//input[contains(@placeholder,'Имя')]"]
    SURNAME_FIELD = [By.XPATH,".//input[contains(@placeholder, 'Фамилия')]"]
    ADRESS_FIELD = [By.XPATH,".//input[contains(@placeholder, 'Адрес')]"]
    PHONE_NUMBER_FIELD = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поле с именем пользователя')
    def fill_in_name_field(self,name):
        self.enter_text(self.NAME_FIELD, name)

    @allure.step('Заполняем поле с фамилией пользователя')
    def fill_in_surname_field(self,surname):
        self.enter_text(self.SURNAME_FIELD, surname)

    @allure.step('Заполняем поле с адресом пользователя')
    def fill_in_adress_field(self,adress):
        self.enter_text(self.ADRESS_FIELD, adress)

    @allure.step('Заполняем поле с телефоном пользователя')
    def fill_in_phone_field(self,phone):
        self.enter_text(self.PHONE_NUMBER_FIELD, phone)

    @allure.step('Заполняем все поля о пользователе')
    def fill_in_all_fields_on_order_page_except_metro(self,name,surname,adress,phone):
        self.fill_in_name_field(name)
        self.fill_in_surname_field(surname)
        self.fill_in_adress_field(adress)
        self.fill_in_phone_field(phone)

    @allure.step('Кликаем на кнопку далее')
    def click_on_next_button(self):
        self.click_element(self.NEXT_BUTTON)

class MetroLocators(BasePage):
    METRO_INPUT = By.XPATH, "//input[@class='select-search__input']"
    def __init__(self, driver):
        self.driver = driver
    @staticmethod
    def get_metro_station_locator(metro):
        return By.XPATH, f"//*[@class='select-search__select']//*[text()='{metro}']"

    @allure.step('Заполняем поле со станцией метро')
    def fill_in_metro_station(self,metro):
        self.enter_text(self.METRO_INPUT, metro)
    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self,metro):
        #self.driver.find_element(*MetroLocators.get_metro_station_locator(metro)).click()
        self.click_element(MetroLocators.get_metro_station_locator(metro))