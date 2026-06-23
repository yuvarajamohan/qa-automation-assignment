from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestCitations(BaseTest):

    def test_citations_present(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        home.select_role("Employee")

        home.ask_question(
            "How many days can I work remotely?"
        )

        citations = home.wait_for_citations()

        self.assertNotEqual(
            citations,
            ""
        )