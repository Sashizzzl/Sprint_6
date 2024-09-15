import allure
from selenium.webdriver.common.by import By
from config import Url
from pages.base_page import BasePage

class MainPage(BasePage):
    ORDER_BUTTON_IN_HEADER = [By.XPATH, './/div[contains(@class,"Header")]/button[text()="Заказать"]']
    ORDER_BUTTON_IN_HOME_AREA =[By.XPATH, ".// div[contains( @ class, 'Home')] / button[text()='Заказать']"]
    def __init__(self, driver):
        self.driver = driver

    #@allure.step('Открываем страницу ЯндексСамокат')
    #def open_page(self):
        #self.navigate(Url.SAMOKAT_URL)

    @allure.step('Кликаем на кнопку заказа в верхней части страницы')
    def click_order_button_in_header(self):
        self.click_element(self.ORDER_BUTTON_IN_HEADER)

    @allure.step('Пролистываем до нижней части страницы')
    def scroll_to_home_area(self):
        self.scroll_to_element(self.ORDER_BUTTON_IN_HOME_AREA)

    @allure.step('Кликаем на кнопку заказа в нижней части страницы')
    def click_on_order_button_in_home_area(self):
        self.click_element(self.ORDER_BUTTON_IN_HOME_AREA)

