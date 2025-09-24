#import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

#    @allure.step('Открыть сайт')
    def go_to_site(self):
        return self.driver.get(self.base_url)
        
#    @allure.step('Найти элемент по локатору {locator}')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
    
#    @allure.step('Найти элементы по локатору {locator}')
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
    
#    @allure.step('Кликнуть на элемент {locator}')
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

#    @allure.step('Ввести текст "{text}" в поле {locator}')
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

#    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

#    @allure.step('Прокрутить до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)