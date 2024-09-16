import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.about_rent_page import AboutRentPage
from config import Url
from pages.order_page import MetroLocators

class TestPlacingOrder:
    @allure.title('Проверка успешного заказа самоката с последующим переходом на главную страницу и страницу ЯндексДзен')
    @pytest.mark.parametrize("name,surname,adress,phone,metro,time",[("Александра","Русакова","Ленина 7","12345678989","Сокольники","01.10.2024"),
                                                                     ("Тейлор","Свифт","5 Авеню","12345678980","Войковская","01.11.2024")])
    def test_placing_order(self,driver,navigate,name,surname,adress,phone,metro,time):
        order = MainPage(driver)
        #проверяем кнопку заказа вверху страницы
        order.close_coockie()
        order.click_order_button_in_header()

        rent = OrderPage(driver)
        rent.fill_in_all_fields_on_order_page_except_metro(name, surname, adress, phone)
        metro_fill_in = MetroLocators(driver)
        metro_fill_in.fill_in_metro_station(metro)
        metro_fill_in.choose_metro_station(metro)
        rent.click_on_next_button()

        rent_page = AboutRentPage(driver)
        rent_page.complete_order_in_rent_page(time)
        value_of_confirmation = rent_page.value_in_confirmation_window()
        assert 'Заказ оформлен' in value_of_confirmation

        rent_page.click_on_see_status_in_confirmation_window()
        rent_page.click_on_samokat_logo()
        current_url = rent_page.get_current_url()
        assert current_url ==Url.SAMOKAT_URL

        #проверяем кнопку заказа внизу страницы
        order.scroll_to_home_area()
        order.order_button_in_home_area_is_present()
        order.click_on_order_button_in_home_area()
        rent = OrderPage(driver)
        rent.fill_in_all_fields_on_order_page_except_metro(name, surname, adress, phone)
        metro_fill_in = MetroLocators(driver)
        metro_fill_in.fill_in_metro_station(metro)
        metro_fill_in.choose_metro_station(metro)
        rent.click_on_next_button()

        rent_page = AboutRentPage(driver)
        rent_page.complete_order_in_rent_page(time)
        value_of_confirmation = rent_page.value_in_confirmation_window()
        assert 'Заказ оформлен' in value_of_confirmation

        rent_page.click_on_see_status_in_confirmation_window()
        rent_page.click_on_yandex_logo()
        rent_page.switch_to_the_last_window()
        rent_page.wait_for_browsing_url_yandex()
        current_url_2 = rent_page.get_current_url()
        assert current_url_2 == Url.YANDEX_URL
