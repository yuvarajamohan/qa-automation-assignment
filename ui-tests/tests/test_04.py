from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestEMEAMeal(BaseTest):

    def test_emea_meal_allowance(self):

        home = HomePage(self.driver)

        home.select_region("EMEA")
        home.select_role("Employee")

        home.ask_question(
            "What is my daily meal allowance?"
        )

        answer = home.wait_for_answer()

        self.assertNotEqual(
            answer,
            ""
        )