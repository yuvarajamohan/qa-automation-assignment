from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestEmployeeRestriction(BaseTest):

    def test_employee_cannot_view_manager_policy(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Employee")

        home.ask_question(
            "What is the compensation review process?"
        )

        answer = home.wait_for_answer()

        self.assertIn(
            "do not have",
            answer
        )