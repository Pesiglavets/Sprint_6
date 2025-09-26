import pytest
import allure
from pages.main_page import MainPage


class TestFAQ:
    @allure.title("Проверка выпадающего списка: {question_text}")
    @pytest.mark.parametrize('question_text,expected_answer_snippet', [
        ("Сколько это стоит? И как оплатить?", "Сутки — 400 рублей"),
        ("Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат"),
        ("Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая"),
        ("Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня"),
        ("Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет"),
        ("Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой"),
        ("Можно ли отменить заказ?", "Да, пока самокат не привезли"),
        ("Я жизу за МКАДом, привезёте?", "Да, обязательно")
    ])
    def test_faq_questions(self, driver, question_text, expected_answer_snippet):
        main_page = MainPage(driver)
        
        main_page.go_to_site()
        main_page.click_accept_cookie_button()
        main_page.scroll_to_faq()
        main_page.click_faq_question_by_text(question_text)
        
        answer_text = main_page.get_faq_answer_by_question_text(question_text)
        
        assert answer_text is not None, f"Ответ на вопрос '{question_text}' не найден"
        assert expected_answer_snippet in answer_text, f"Ответ на вопрос '{question_text}' не содержит '{expected_answer_snippet}'"