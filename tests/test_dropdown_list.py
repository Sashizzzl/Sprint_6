import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.dropdown_list_page import DropdownList
from config import Url
class TestDropdownList:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка соотвествия текста элементов выпадающего списка')
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_on_element_of_dropdown_list_element_opened_with_correct_text(self,index):
        drop_down_list = DropdownList(self.driver)

        drop_down_list.open_page()
        drop_down_list.scroll_to_dropdown_list(index)
        drop_down_list.wait_till_element_is_clickable(index)
        drop_down_list.click_on_element_of_list(index)
        text = ('Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.','Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
        value_of_text= drop_down_list.value_in_text_of_element(index)

        assert value_of_text == text[index]

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
