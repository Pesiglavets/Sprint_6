import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators, FAQPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать кнопку "да все привыкли"')
    def click_accept_cookie_button(self):
        self.click_element(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Прокрутить до раздела FAQ')
    def scroll_to_faq(self):
        self.scroll_to_element(FAQPageLocators.FAQ_SECTION)

    @allure.step('Найти вопрос по тексту "{question_text}"')
    def _find_question_element(self, question_text):
        questions = self.find_elements(FAQPageLocators.FAQ_QUESTIONS)
        for question in questions:
            if question.text == question_text:
                return question
        raise ValueError(f"Вопрос с текстом '{question_text}' не найден")

    @allure.step('Найти ответ соответствующий вопросу "{question_text}"')
    def _find_answer_element(self, question_text):
        questions = self.find_elements(FAQPageLocators.FAQ_QUESTIONS)
        answers = self.find_elements(FAQPageLocators.FAQ_ANSWERS)
        
        for i, question in enumerate(questions):
            if question.text == question_text:
                if i < len(answers):
                    return answers[i]
                else:
                    raise ValueError(f"Для вопроса '{question_text}' не найден ответ")
        raise ValueError(f"Вопрос с текстом '{question_text}' не найден")

    @allure.step('Кликнуть на вопрос FAQ по тексту "{question_text}"')
    def click_faq_question_by_text(self, question_text):
        question = self._find_question_element(question_text)
        question.click()

    @allure.step('Получить ответ на вопрос "{question_text}"')
    def get_faq_answer_by_question_text(self, question_text):
        answer_element = self._find_answer_element(question_text)
        return answer_element.text