import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data_set import TestData


class TestOrderScooter:
    @allure.title("Проверка заказа самоката через {order_button_type} кнопку")
    @pytest.mark.parametrize('data_set,order_button_type,order_button_method', [
        (TestData.ORDER_DATA_SET_1, "верхнюю", "click_top_order_button"),
        (TestData.ORDER_DATA_SET_2, "нижнюю", "click_bottom_order_button")
    ])
    def test_order_scooter_positive_flow(self, driver, data_set, order_button_type, order_button_method):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.go_to_site()
        
        # Используем getattr для вызова метода по имени
        order_button_method = getattr(main_page, order_button_method)
        order_button_method()
        
        order_page.fill_first_page(
            data_set['name'],
            data_set['surname'],
            data_set['address'],
            data_set['metro_station'],
            data_set['phone']
        )
        
        order_page.fill_second_page(
            data_set['delivery_day'],
            data_set['rental_period'],
            data_set['color'],
            data_set['comment']
        )
        
        order_page.confirm_order()
        
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message, "Сообщение об успешном заказе не отображается"

    @allure.title("Проверка перехода на главную страницу через логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        main_page.go_to_site()
        main_page.click_scooter_logo()
        
        current_url = main_page.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        main_page.go_to_site()
        
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        
        main_page.switch_to_new_window(original_window)
        
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        current_url = driver.current_url
        assert "dzen.ru" in current_url, f"Ожидался dzen.ru, но получен {current_url}"