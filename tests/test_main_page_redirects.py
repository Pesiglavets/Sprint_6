import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class TestMainPageRedirects:
    @allure.title("Проверка перехода на главную страницу через логотип Самоката")
    def test_scooter_logo_redirect_to_main(self, driver):
        main_page = MainPage(driver)
        
        main_page.go_to_site()
        main_page.click_scooter_logo()
        
        current_url = main_page.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        
        main_page.go_to_site()
        
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        
        main_page.switch_to_new_window(original_window)
        
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        current_url = driver.current_url
        assert "dzen.ru" in current_url, f"Ожидался dzen.ru, но получен {current_url}"