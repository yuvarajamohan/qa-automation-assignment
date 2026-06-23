from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestRemoteWork(BaseTest):

    def test_remote_work_policy(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Employee")

        home.ask_question(
            "How many days can I work remotely?"
        )

        answer = home.wait_for_answer()

        self.assertNotEqual(
            answer,
            ""
        )