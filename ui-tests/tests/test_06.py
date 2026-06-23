from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestManagerPolicy(BaseTest):

    def test_manager_policy(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Manager")

        home.ask_question(
            "What is the compensation review process?"
        )

        answer = home.wait_for_answer()

        self.assertNotEqual(
            answer,
            ""
        )