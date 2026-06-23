from utils.base_test import BaseTest
from pages.home_page import HomePage
from selenium.webdriver.support.ui import Select
import time


class TestRegionSwitch(BaseTest):

    def test_region_switching(self):

        home = HomePage(self.driver)

        home.select_region("Americas")
        time.sleep(2)

        selected = Select(
            self.driver.find_element(
                *home.REGION
            )
        ).first_selected_option.text

        self.assertEqual(
            selected,
            "Americas"
        )

        home.select_region("EMEA")
        time.sleep(2)

        selected = Select(
            self.driver.find_element(
                *home.REGION
            )
        ).first_selected_option.text

        self.assertEqual(
            selected,
            "EMEA"
        )

        home.select_region("APAC")
        time.sleep(2)

        selected = Select(
            self.driver.find_element(
                *home.REGION
            )
        ).first_selected_option.text

        self.assertEqual(
            selected,
            "APAC"
        )