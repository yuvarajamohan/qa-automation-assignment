from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestProcurement(BaseTest):

    def test_procurement_policy(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Finance")

        home.ask_question(
            "What are the procurement approval thresholds?"
        )

        answer = home.wait_for_answer()

        self.assertNotEqual(
            answer,
            ""
        )