import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step('Выбрать станцию метро "{station}"')
    def select_metro_station(self, station):
        self.click_element(self.locators.METRO_STATION_INPUT)
        station_locator = (By.XPATH, f"//div[text()='{station}']")
        self.click_element(station_locator)

    @allure.step('Выбрать срок аренды "{period}"')
    def select_rental_period(self, period):
        self.find_element(self.locators.RENTAL_PERIOD_DROPDOWN)        
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        period_locator = (By.XPATH, f"//div[text()='{period}']")
        self.find_element(period_locator)             
        self.click_element(period_locator)

    @allure.step('Выбрать цвет самоката "{color}"')
    def select_color(self, color):
        if color == "black":
            self.click_element(self.locators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(self.locators.GREY_CHECKBOX)
        else:
            raise ValueError(f"Неизвестный цвет: {color}")
        
    @allure.step('Выбрать дату доставки: {day} число')
    def select_delivery_date(self, day):
        self.find_element(self.locators.DELIVERY_DATE_INPUT)        
        self.click_element(self.locators.DELIVERY_DATE_INPUT)
        day_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")        
        self.find_element(day_locator)        
        self.click_element(day_locator)

    @allure.step('Заполнить первую страницу заказа')
    def fill_first_page(self, name, surname, address, metro_station, phone):
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.SURNAME_INPUT, surname)
        self.input_text(self.locators.ADDRESS_INPUT, address)
        self.select_metro_station(metro_station)
        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step('Заполнить вторую страницу заказа')
    def fill_second_page(self, delivery_day, rental_period, color, comment):
        self.select_delivery_date(delivery_day)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.input_text(self.locators.COMMENT_INPUT, comment)
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step('Получить сообщение об успешном заказе')
    def get_success_message(self):
        return self.find_element(self.locators.SUCCESS_MESSAGE).text