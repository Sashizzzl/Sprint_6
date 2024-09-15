import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutRentPage(BasePage):
    TIME_FIELD = [By.XPATH,".//input[contains(@placeholder,'Когда')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH,".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_ONE_DAY = [By.XPATH, ".//div[contains(@class,'Dropdown-option') and contains(text(),'сутки')]"]
    ORDER_BUTTON = [By.XPATH,".//div[contains(@class, 'Order')]/button[text()='Заказать']"]
    BUTTON_YES_IN_POP_UP_DO_YOU_WANT_TO_ORDER = [By.XPATH,".//button[text()='Да']"]
    ORDER_IS_PLACED = [By.XPATH,".//div[contains(@class,'Order_ModalHeader')]"]
    BUTTON_TO_SEE_STATUS_IN_PUP_UP_ORDER_IS_PLACED = [By.XPATH, ".//button[text()='Посмотреть статус']"]
    SAMOKAT_LOGO = [By.XPATH, ".//img[@alt='Scooter']"]
    YANDEX_LOGO = [By.XPATH, ".//img[@alt='Yandex']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поле со временем доставки')
    def fill_in_time_field(self, time):
        self.enter_text(self.TIME_FIELD, time)

    @allure.step('Заполняем поле с периодом аренды')
    def click_on_rental_period_field(self):
        self.click_element(self.RENTAL_PERIOD_FIELD)

    @allure.step('Выбираем период аренды')
    def choose_rental_period_time(self):
        self.click_element(self.RENTAL_PERIOD_ONE_DAY)

    @allure.step('Кликаем на кнопку заказать')
    def click_on_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step('Кликаем на кнопку заказать')
    def confirm_order(self):
        self.click_element(self.BUTTON_YES_IN_POP_UP_DO_YOU_WANT_TO_ORDER)

    @allure.step('Заполняем все обязательные поля в окне заказа и подтверждаем заказ')
    def complete_order_in_rent_page(self,time):
        self.fill_in_time_field(time)
        self.click_on_rental_period_field()
        self.choose_rental_period_time()
        self.click_on_order_button()
        self.confirm_order()

    @allure.step('Получаем значение из окна подтверждения заказа')
    def value_in_confirmation_window(self):
        return self.get_text_of_element(self.ORDER_IS_PLACED)

    @allure.step('Нажимаем на кнопку посмотреть статус')
    def click_on_see_status_in_confirmation_window(self):
        self.click_element(self.BUTTON_TO_SEE_STATUS_IN_PUP_UP_ORDER_IS_PLACED)

    @allure.step('Клик на лого Самокат')
    def click_on_samokat_logo(self):
        self.click_element(self.SAMOKAT_LOGO)

    @allure.step('Клик на лого Яндекс')
    def click_on_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url


