import pytest
import allure
from selenium import webdriver
from pages.dropdown_list_page import DropdownList
class TestDropdownList:
    @allure.title('Проверка соотвествия текста элементов выпадающего списка')
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_on_element_of_dropdown_list_element_opened_with_correct_text(self,driver,navigate,index):
        drop_down_list = DropdownList(driver)


        drop_down_list.scroll_to_dropdown_list(index)
        drop_down_list.wait_till_element_is_clickable(index)
        drop_down_list.click_on_element_of_list(index)
        value_of_text= drop_down_list.value_in_text_of_element(index)

        assert value_of_text == DropdownList.text[index]
