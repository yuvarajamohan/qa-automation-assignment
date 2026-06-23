from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestWeatherRefusal(BaseTest):

    def test_weather_question_refused(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Employee")

        home.ask_question(
            "What is the weather in Chennai today?"
        )

        answer = home.wait_for_answer()

        self.assertIn(
            "do not have",
            answer
        )