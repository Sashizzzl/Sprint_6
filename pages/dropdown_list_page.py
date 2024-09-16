import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Url

class DropdownList:
    elements_of_list= [(By.ID, 'accordion__heading-0'),(By.ID, 'accordion__heading-1'),(By.ID, 'accordion__heading-2'),(By.ID, 'accordion__heading-3'), (By.ID, 'accordion__heading-4'), (By.ID, 'accordion__heading-5'), (By.ID, 'accordion__heading-6'), (By.ID, 'accordion__heading-7')]
    text_of_elements = [(By.ID, 'accordion__panel-0'),(By.ID, 'accordion__panel-1'),(By.ID, 'accordion__panel-2'),(By.ID, 'accordion__panel-3'), (By.ID, 'accordion__panel-4'), (By.ID, 'accordion__panel-5'), (By.ID, 'accordion__panel-6'), (By.ID, 'accordion__panel-7')]
    text = ('Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу ЯндексСамокат')
    def open_page(self):
        self.driver.get(Url.SAMOKAT_URL)
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


