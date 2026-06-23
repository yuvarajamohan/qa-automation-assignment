from utils.base_test import BaseTest
from pages.home_page import HomePage
from selenium.webdriver.support.ui import Select
import time


class TestRoleDropdown(BaseTest):

    def test_role_switching(self):

        home = HomePage(self.driver)

        roles = [
            "Employee",
            "Engineering",
            "Finance",
            "Manager"
        ]

        dropdown = Select(
            self.driver.find_element(
                *home.ROLE
            )
        )

        for role in roles:

            dropdown.select_by_visible_text(
                role
            )

            time.sleep(2)

            selected = dropdown.first_selected_option.text

            self.assertEqual(
                selected,
                role
            )