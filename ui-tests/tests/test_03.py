from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestAmericasMeal(BaseTest):

    def test_americas_meal_allowance(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Employee")

        home.ask_question(
            "What is my daily meal allowance?"
        )

        answer = home.wait_for_answer()

        self.assertIn(
            "USD",
            answer
        )