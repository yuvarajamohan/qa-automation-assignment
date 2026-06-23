from utils.base_test import BaseTest
from pages.home_page import HomePage


class TestEngineeringPolicy(BaseTest):

    def test_engineering_document(self):

        home = HomePage(self.driver)

        
        home.select_region("Americas")

        
        home.select_role("Engineering")

        
        home.ask_question(
            "What is the production data handling standard?"
        )

        
        answer = home.wait_for_answer()

        
        self.assertNotEqual(
            answer,
            ""
        )